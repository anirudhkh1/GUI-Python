aa = {'a': {'F_Name': 'Anirudh', 'L_Name': 'Khurana', 'DOB': '2018-02-06', 'Gender': 'Male',
            'Email_ID': 'anirudh@gmail.com',
            'ph_no': '8956856589', '10_percent': '88', '12_percent': '89', 'Password': 'a', 'Status': 'no'},
      'xnirudh': {'F_Name': 'Anirudh', 'L_Name': 'Khurana', 'DOB': '2018-02-21', 'Gender': 'Male',
                  'Email_ID': 'anirudh7878@gmail.com', 'ph_no': '5566556655', '10_percent': '88', '12_percent': '55',
                  'Password': 'a', 'Status': 'no'},
      'v': {'F_Name': 'ani', 'L_Name': 'dawda', 'DOB': '2018-02-07', 'Gender': 'Male', 'Email_ID': 'dwa@daw.com',
            'ph_no': '5566889955', '10_percent': '66', '12_percent': '88', 'Password': 'a', 'Status': 'no'},
      'dadwa': {'F_Name': 'dwadwad', 'L_Name': 'dwadwad', 'DOB': '2018-02-13', 'Gender': 'Male',
                'Email_ID': 'dwad@dwa.com',
                'ph_no': '5689856589', '10_percent': '88', '12_percent': '55', 'Password': 'dwadwa', 'Status': 'no'},
      'khnna': {'F_Name': 'Anirudh', 'L_Name': 'Khurana', 'DOB': '2018-02-15', 'Gender': 'Male',
                'Email_ID': 'anirudh7878@gmail.com', 'ph_no': '9712928280', '10_percent': '88', '12_percent': '89',
                'Password': '12345678', 'Status': 'no'},
      'lloo': {'F_Name': 'Anirudh', 'L_Name': 'Khurana', 'DOB': '2018-02-13', 'Gender': 'Male',
               'Email_ID': 'dwad@dwa.com',
               'ph_no': '8985658985', '10_percent': '88', '12_percent': '95', 'Password': '123456789', 'Status': 'no'}}

aaa = [a for a in aa.keys()]
aaaa=[]
aaaa.clear()
for i in aaa:
    aaaa.append(aa[i]["F_Name"])
print(aaaa)
