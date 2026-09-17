import streamlit as st
import tempfile
import os


from resume_parser import extract_resume_text
from text_cleaner import clean_text
from skill_extractor import load_skill_dictionary, extract_skills
from job_matcher import load_job_roles, calculate_all_match_scores
from roadmap_generator import generate_roadmap
from section_detector import detect_sections
from resume_score import calculate_completeness_score
from resume_analyzer import count_projects, detect_experience, count_certifications


st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


st.title("📄 AI Resume Analyzer")

st.write(
    "Upload your resume to analyze your skills "
    "and discover suitable job roles."
)


uploaded_file = st.file_uploader(
    "Upload your resume",
    type=["pdf", "docx"]
)


if uploaded_file is not None:

    st.success(
        f"Uploaded: {uploaded_file.name}"
    )

    if st.button("Analyze Resume"):

        # Create a temporary file
        suffix = os.path.splitext(
            uploaded_file.name
        )[1]

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=suffix
        ) as temp_file:

            temp_file.write(
                uploaded_file.getbuffer()
            )

            temp_file_path = temp_file.name

        try:

            # ----------------------------------------
            # 1. Extract resume text
            # ----------------------------------------

            raw_text = extract_resume_text(
                temp_file_path
            )


            # ----------------------------------------
            # 2. Clean resume text
            # ----------------------------------------

            cleaned_text = clean_text(
                raw_text
            )


            # ----------------------------------------
            # 3. Display extracted text
            # ----------------------------------------

            st.subheader("📄 Extracted Resume Text")

            st.text_area(
                "Resume Content",
                cleaned_text,
                height=300
            )


            # ----------------------------------------
            # 4. Extract skills
            # ----------------------------------------

            skill_dictionary = load_skill_dictionary()

            resume_skills = extract_skills(
                cleaned_text,
                skill_dictionary
            )
            sections = detect_sections(cleaned_text)
            project_count = count_projects(cleaned_text)
            experience_found = detect_experience(cleaned_text)
            certification_count = count_certifications(cleaned_text)

            st.subheader("📊 Resume Content")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Projects Detected",
                    project_count
                )

            with col2:
                st.metric(
                    "Experience",
                    "Found" if experience_found else "Not Found"
                )

            with col3:
                st.metric(
                    "Certification Evidence",
                    certification_count
                )
            completeness_score = calculate_completeness_score(sections)

            st.subheader("📋 Resume Completeness")

            st.metric(
                label="Completeness Score",
                value=f"{completeness_score}%"
            )

            if completeness_score == 100:
                st.success("🎉 All important resume sections were detected!")
            elif completeness_score >= 70:
                st.info("👍 Your resume has most important sections.")
            else:
                st.warning("⚠️ Some important resume sections are missing.")

            st.subheader("📋 Resume Sections")

            section_names = {
                "summary": "Profile / Summary",
                "education": "Education",
                "experience": "Experience",
                "projects": "Projects",
                "skills": "Skills",
                "certifications": "Certifications"
            }

            for section, found in sections.items():
             if found:
                 st.success(f"✓ {section_names[section]}")
            else:
                 st.warning(f"✗ {section_names[section]} not detected")


            st.subheader("🛠️ Skills Detected")

            if resume_skills:

                for skill in resume_skills:
                    st.write(f"✓ {skill}")

            else:

                st.warning(
                    "No skills detected."
                )


            # ----------------------------------------
            # 5. Load job roles
            # ----------------------------------------

            job_roles = load_job_roles()


            # ----------------------------------------
            # 6. Calculate all matching scores
            # ----------------------------------------

            results = calculate_all_match_scores(
                cleaned_text,
                resume_skills,
                job_roles
            )


            # ----------------------------------------
            # 7. Show top 3 recommended roles
            # ----------------------------------------

            st.subheader(
                "🎯 Recommended Job Roles"
            )
            best_role_score = results[0]["final_score"]

            overall_score = round(
            (completeness_score * 0.40) +
            (best_role_score * 0.60),
            2
            )

            st.subheader("📈 Overall Resume Score")

            score_col1, score_col2, score_col3 = st.columns(3)

            with score_col1:
             st.metric(
                "Completeness",
                f"{completeness_score}%"
            )

            with score_col2:
                st.metric(
                "Best Job Match",
                f"{best_role_score}%"
            )

            with score_col3:
                st.metric(
                "Overall Strength",
                f"{overall_score}%"
            )     

            if overall_score >= 75:
                st.success("Excellent resume match!")
            elif overall_score >= 50:
                st.info("Good resume match. Some skills can be improved.")
            elif overall_score >= 30:
                st.warning("Moderate match. Consider improving the missing skills.")
            else:
                st.error("Low match. Focus on the recommended learning roadmap.")
                st.subheader("📊 Role Match Comparison")

            chart_data = {
                "Role": [result["role"] for result in results[:3]],
                "Skill Match": [result["skill_score"] for result in results[:3]],
                "TF-IDF": [result["tfidf_score"] for result in results[:3]],
                "Semantic Match": [result["semantic_score"] for result in results[:3]],
                "Final Score": [result["final_score"] for result in results[:3]]
            }

            st.bar_chart(
                chart_data,
                x="Role",
                y=["Skill Match", "TF-IDF", "Semantic Match", "Final Score"]
            )

            for rank, result in enumerate(
                results[:3],
                start=1
            ):

                st.markdown(
                    f"### {rank}. {result['role']}"
                )

                st.progress(
                    int(result["final_score"])
                )

                st.write(
                    f"**Final Match Score: "
                    f"{result['final_score']}%**"
                )

                st.write(
                    f"Skill Match: "
                    f"{result['skill_score']}%  |  "
                    f"TF-IDF: "
                    f"{result['tfidf_score']}%  |  "
                    f"Semantic: "
                    f"{result['semantic_score']}%"
                )
                # Show matched skills
                with st.expander("✅ Matched Skills"):

                    if result["matched_skills"]:

                        for skill in result["matched_skills"]:
                            st.write(f"✓ {skill}")

                    else:

                        st.write("No required skills matched.")


                    # Show missing skills
                with st.expander("⚠️ Missing Skills"):

                    if result["missing_skills"]:

                        for skill in result["missing_skills"]:
                            st.write(f"✗ {skill}")

                    else:

                        st.write("No missing skills!")
                with st.expander("📚 Learning Roadmap"):
                    roadmap = generate_roadmap(result["missing_skills"])

                    if roadmap:
                        for item in roadmap:
                            st.markdown(f"**{item['skill']}**")
                            st.write(item["recommendation"])
                    else:
                         st.write("🎉 No roadmap needed. You have all the required skills!")
                with st.expander("💡 Why this role?"):
                    matched_count = len(result["matched_skills"])
                    missing_count = len(result["missing_skills"])

                    st.write(
                        f"Your resume matches **{matched_count} required skills** "
                        f"and is missing **{missing_count} skills** for this role."
                    )

                    if result["final_score"] >= 70:
                        st.success(
                        "This role is a strong match for your current resume."
                    )
                    elif result["final_score"] >= 50:
                        st.info(
                        "This role is a reasonable match, but improving the missing "
                        "skills could significantly strengthen your profile."
                    )
                    else:
                        st.warning(
                        "This role currently has a lower match. Focus on the "
                        "missing skills in the learning roadmap."
                    )


        finally:

            # Delete temporary file
            if os.path.exists(temp_file_path):

                os.remove(
                    temp_file_path
                )