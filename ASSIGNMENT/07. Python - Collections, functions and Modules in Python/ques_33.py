# Q.33 Write a Python script to concatenate following dictionaries to create a new one. 

Details = {

            'IMROZ':{
                'mobile':['1234567890'],
                'email':'IMROZ@gmail.com',
                'batch':'Full Stack Development'
                }
         }       

Details2 = {
            
            'AADIL':{
                'mobile':['5498763210','4578963210'],
                'email':'AADIL@gmail.com',
                'batch':'UI/UX design'
    
           }
}

Details.update(Details2)
print(Details)

