# Q.38 Write a Python script to merge two Python dictionaries.

Details = {

            'imroz':{
                'mobile':['2123545856'],
                'email':'imroz@gmail.com',
                'batch':'FSD python'
                }
         }       

Details2 = {
            
            'aadil':{
                'mobile':['1233214567','2334545667'],
                'email':'aadil@gmail.com',
                'batch':'frontend'
    
           }
}

Details.update(Details2)
print(Details)
