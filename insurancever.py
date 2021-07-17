age = input("Applicant age: ")
if 18 <= int(age) <= 64:
    print("Eligible.")
elif int(age) < 18:
        print(f"Applicant is {18 - int(age)} years under feasible age, individual is not eligible.")
elif int(age) > 64:
        print(f"Applicant is {int(age) - 64} years above feasible age, individual is not eligible.")
