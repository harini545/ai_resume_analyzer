from combined_matcher import calculate_final_score


# Example scores
skill_score = 57.14
tfidf_score = 7.65
semantic_score = 35.42


final_score = calculate_final_score(
    skill_score,
    tfidf_score,
    semantic_score
)


print("\n========== COMBINED MATCH SCORE ==========")
print(f"Skill Score: {skill_score}%")
print(f"TF-IDF Score: {tfidf_score}%")
print(f"Semantic Score: {semantic_score}%")
print(f"Final Match Score: {final_score}%")