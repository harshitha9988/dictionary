student_data={'idl':
              {'name':['Sara'],
               'class':['V'],
               'subject_integration': ['english, science, math']
              },
              'id2':
               {'name':['David'],
               'class':['V'],
               'subject_integration': ['english, science, math']
              },

              'id3':
               {'name':['Sara'],
               'class':['V'],
               'subject_integration': ['english, science, math']
              },

              'id4':
               {'name':['Ella'],
               'class':['V'],
               'subject_integration': ['english, science, math']
              },

}  
            
result={}

for key, value in student_data.items():
    if value not in result.values():
        result[key]=value

print(result)