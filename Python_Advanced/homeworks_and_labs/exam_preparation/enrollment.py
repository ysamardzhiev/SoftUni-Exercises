def gather_credits(needed_credits, *courses):
    enrolled_courses = []
    gathered_credits = 0

    for course, credits in courses:

        if needed_credits > gathered_credits:
            if course in enrolled_courses:
                continue
            enrolled_courses.append(course)
            gathered_credits += credits
        else:
            break

    if gathered_credits >= needed_credits:
        return f"Enrollment finished! Maximum credits: {gathered_credits}.\n" \
               f"Courses: {', '.join(sorted(enrolled_courses))}"
    else:
        return f"You need to enroll in more courses! " \
               f"You have to gather {needed_credits - gathered_credits} credits more."


print(gather_credits(
    80,
    ("Basics", 27),
))

print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))

print(gather_credits(
    60,
    ("Basics", 27),
    ("Advanced", 27),
    ("Advanced", 30),
    ("Web", 30)
))

