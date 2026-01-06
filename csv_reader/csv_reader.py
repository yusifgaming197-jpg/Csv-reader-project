import csv

def process_students_data(file_path):
    try:
        with open(file_path, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            rows = list(reader)
    
            if not rows:
                print('Error: CSV file is empty')
                return
        
            print(f"{'Name':<15} | {'Age':<5} | {'Score':<5}")
            print('-' * 35)
        
            total = 0 
            high = []
            middle = []
            low = []
            
            for row in rows:
                name = row['name']   
                age = row['age']          
                score = int(row['score'])        
            
                # format  table row
                print(f"{name:<15} | {age:<5} | {score:<5}")    
            
                total += score
             
                if score >= 80:
                    high.append(f"{name} ({score})")
                elif score <= 70 :
                    low.append(f"{name} ({score})")        
                else:
                    middle.append(f"{name} ({score})")      
            
            # Summary
            print('\n' + '=' * 35)  
            print(f'total students: {len(rows)}')   
            print(f'average Score:  {total / len(rows):.2f}') 
            print('=' * 35)
        
            print(f"\nstudents 80 Score: {', '.join(high)}")   
            print(f"students below 80:  {', '.join(middle)}")
            print(f"students below  or equal to 70:  {', '.join(low)}")
            
    except FileNotFoundError:
        print(f"Error: the file '{file_path}' was not found.")
    except KeyError as e:
        print(f"Error: missing column in CSV: {e}")
    except ValueError:
        print(f"Error: invalid data found. Ensure scores are numbers.")   
         
if __name__ == '__main__':
    process_students_data("students.csv")
