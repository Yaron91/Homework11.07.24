iq_before: int = int (input("Enter the IQ number of a student before studying: "));
sum_before: int = 0
count_before: int =0
while iq_before > 30 and iq_before < 300:
    sum_before = sum_before + iq_before
    count_before = count_before + 1;
    iq_before: int = int(input("Enter another IQ number of a student before studying: "));
if count_before > 0: #this is to ensure the code can handle division by 0
    avg_before: float = float (sum_before/count_before);
    print(f"The average IQ of the study group before studying is {avg_before}");
else:
    print ("Not a single valid number was added...");

print (" One year of Python training has been completed...")

iq_after: int = int (input("Enter the IQ number of a student before studying: "));
sum_after: int = 0
count_after: int =0
while iq_after > 30 and iq_after < 300:
    sum_after = sum_after + iq_after
    count_after = count_after + 1;
    iq_after: int = int(input("Enter another IQ number of a student before studying: "));
if count_after > 0:
    avg_after: float = float (sum_after/count_after);
    print(f"The average IQ of the study group after studying is {avg_after}");
else:
    print ("Not a single valid number was added...");

print (f"The average IQ of the students after studying grew by {avg_after - avg_before} points" if avg_after > avg_before else f"The average IQ of the students was higher before studying by {avg_before - avg_after} points")