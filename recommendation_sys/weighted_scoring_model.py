#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import math

careers = pd.read_csv('data/data.csv')
course_to_skill = pd.read_csv('data/courses_to_skills.csv')
course_to_skills = pd.read_csv('data/courses_to_skills.csv')
students_transcript = pd.read_csv('data/students_transcript.csv')

know_skills_to_career = pd.read_csv('data/Knowledge_skills.csv')
know_skills_to_career.pop("Unnamed: 0")
know_skills_to_career

personality_to_career = pd.read_csv('data/Personality.csv')
personality_to_career.pop("Unnamed: 0")
personality_to_career

careerList = know_skills_to_career['Title'].values.tolist()

careers.pop("Unnamed: 0")

career_dic = careers.to_dict()

grades_of_all_stud = [student_rec[1:] for student_rec in students_transcript.values.tolist()]
courses_to_skills = [course_skill[1:] for course_skill in course_to_skills.values.tolist()]
career_person = personality_to_career.values.tolist()
career_know_skill = know_skills_to_career.values.tolist()

career_pers = [career_person[i][:-1] for i in range(len(career_person))]
career_personality = [[(num*5/7) for num in numbers] for numbers in career_pers]





def career_know_skill_personality(student_id,personality_result):
    student_id = int(student_id)
    no_of_skills = len(know_skills_to_career.columns.tolist()) - 1
    list_of_courses = course_to_skills.columns.tolist()
    list_of_courses.pop(0)
    list_of_careers = know_skills_to_career['Title'].values.tolist()


    courses_to_skills = [course_skill[1:] for course_skill in course_to_skills.values.tolist()]

    KSP_to_careers = [career_know_skill[i][:-1] + career_personality[i][:] for i in range(len(career_personality))]
    student_skills_set_average = list()

    for skill_no in range(no_of_skills):
        temp = 0
        stud_record = grades_of_all_stud[student_id][1:]
        total_expert_rating = 0

        for course_no in range(len(stud_record)):
            score = stud_record[course_no]/100
            expert_rating  = courses_to_skills[skill_no][course_no+1]
            temp += score*expert_rating
            total_expert_rating += expert_rating

        student_skills_set_average.append(temp/total_expert_rating)

    stud_skill_personality = student_skills_set_average + personality_result


    no_of_careers = len(list_of_careers)
    career_rankings = []
    for i in range(no_of_careers):
        temp = 0
        total_career_KSP = 0
        for j in range(len(stud_skill_personality)):

            stud_skill_personality_val = stud_skill_personality[j]
            career_KSP_val = KSP_to_careers[i][j]
            temp += stud_skill_personality_val * career_KSP_val
            total_career_KSP += career_KSP_val

        career_rankings.append(temp/total_career_KSP)      #[ranking of all careers]

    # next function to identify rankings or
    top_10_for_student_id = sorted(range(len(career_rankings)), key=lambda k: career_rankings[k])
    top_10_for_student_id.reverse()
    careerdes = [career_dic['Description'][i]for i in top_10_for_student_id[:10]]
    print(top_10_for_student_id)
    print(career_rankings)
    return  [(careerList[i], career_dic['Description'][i]) for i in top_10_for_student_id[:10]]



def career_acad(student_id):
    stud_id = int(student_id)

    no_of_skills = len(know_skills_to_career.columns.tolist()) - 1
    list_of_courses = course_to_skills.columns.tolist()
    list_of_courses.pop(0)
    list_of_careers = know_skills_to_career['Title'].values.tolist()

    courses_to_skills = [course_skill[1:] for course_skill in course_to_skills.values.tolist()]
    skills_to_careers = [career_skill[:-1] for career_skill in know_skills_to_career.values.tolist()]

    student_skills_set_average =[]

    for skill_no in range(no_of_skills):
        temp = 0
        stud_rec = grades_of_all_stud[stud_id][1:]
        total_expert_rating = 0
        for course_no in range(len(stud_rec)):
            score = stud_rec[course_no]/100
            expert_rating = courses_to_skills[skill_no][course_no+1]
            temp += score*expert_rating
            total_expert_rating += expert_rating

        student_skills_set_average.append(temp/total_expert_rating)

    no_of_careers = len(list_of_careers)
    career_rankings = list()

    for i in range(no_of_careers):
        temp = 0
        total_career_KS = 0

        for j in range(len(student_skills_set_average)):
            stud_skill_val = student_skills_set_average[j]
            career_skill_val = skills_to_careers[i][j]
            temp += stud_skill_val * career_skill_val
            total_career_KS += career_skill_val

        career_rankings.append(temp/total_career_KS)      #[ranking of all careers]

    # next function to identify rankings or 
    top_10_for_student_id = sorted(range(len(career_rankings)), key=lambda k: career_rankings[k])
    top_10_for_student_id.reverse()
    print(career_dic)
    careerdes = [career_dic['Description'][i]for i in top_10_for_student_id[:10]]
    print(career_rankings)
    # print(top_10_for_student_id[:10])
    top = [careerList[i]for i in top_10_for_student_id[:10]]
    return  [(index+1,careerList[i], career_dic['Description'][i]) for index, i in enumerate(top_10_for_student_id[:10])]





def career_person(student_id, personality_result):
    student_id = int(student_id)

    no_of_personality = len(personality_to_career.columns.tolist()) -1
    list_of_careers = know_skills_to_career['Title'].values.tolist()
    student_skills_set_average =[]
    print(len(career_personality))
    no_of_careers = len(list_of_careers)
    career_rankings = []
    for i in range(no_of_careers):
        temp = 0
        total_career_personality = 0
        for j in range(len(personality_result)):
            stud_personality_val = personality_result[j]
            career_personality_val = career_personality[i][j]
            temp += stud_personality_val * career_personality_val
            total_career_personality += career_personality_val

        career_rankings.append(temp/total_career_personality)      #[ranking of all careers]

    # next function to identify rankings or
    top_10_for_student_id = sorted(range(len(career_rankings)), key=lambda k: career_rankings[k])
    top_10_for_student_id.reverse()
    careerdes = [career_dic['Description'][i]for i in top_10_for_student_id[:10]]
    print(career_rankings)
    print(top_10_for_student_id[:10])
    return  [(careerList[i], career_dic['Description'][i]) for i in top_10_for_student_id[:10]]




