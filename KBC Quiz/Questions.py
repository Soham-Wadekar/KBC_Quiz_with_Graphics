import numpy as np

# Questions List

easy_ques = ['Which animal is known as the "Ship of the Desert"?','Who designed the National Flag of India?','The largest planet in our Solar System is: ','Name the National tree of India.','Which is the tallest mountain in North America?','In the Hindu epic of Ramayana, what kind of bird was Jatayu?','The ozone layer restricts:','Which metal is used for galvanizing iron?','India’s first satellite is named after:',"Where is 'The Leaning Tower of Pisa' located?",'What is the currency of Australia?','Who was the first man to walk on the Moon?','The longest river in the world is: ','Which bird lays the largest eggs?',"A 'Decagon' is a shape with __ sides.",'']

med_ques = ['Which telescope was launched into space in late December of 2021?','Who defeated the Marathas in the third battle of Panipat?','Which country is known as ‘The Land of the Rising Sun’?','Who was the first woman in the world to go to space?','In which year were the Olympic Games cancelled due to World War 1?','Entomology is the study of:','Golf player Vijay Singh belongs to which country?','For the Olympics and World Tournaments, the dimensions of basketball court are:','Durand Cup is associated with:','What is ‘a seismograph’ used to measure?','Malaria is caused by:','What is the capital of Kenya?','Film and Television Institute of India is located at:','Hockey was introduced in the Asian Games in:','In which year, the first meeting of Rajya Sabha was held in Independent India?','']

hard_ques = ['The smallest bone in the human body is:','Who created the first watch?','Who first translated the Bhagvad Gita to English?','The Ashes Cup was first played in this stadium in London:','Who won the Nobel Prize in Physics in 2017 for his work in LIGO?','During the first crusade, crusaders reached Jerusalem and captured it in:','Each year World Red Cross and Red Crescent Day is celebrated on','Germany signed the Armistice Treaty on ____ and World War I ended','Who was the first Indian Chief of Army Staff of the Indian Army?','Hamid Karzai was chosen president of Afghanistan in:','']

flip_ques = ['The first Indian leader to undergo imprisonment was:','On which day, did terrorists crashed a plane into the World Trade Centre?','Indira Gandhi was assassinated in:','How many players are there on each side in Basketball?','In Cricket, the two stumps are ________ apart.']

# Options List

optA_easy = ['Horse','Pingali Venkayya','Uranus','Mango Tree','Mt Fuji','Kite','Visible light','Aluminium','Aryabhatta','France','Australian Dollar','Micheal Collins','Mississippi','Vulture','10']

optB_easy = ['Donkey','Mahatma Gandhi','Saturn','Coconut Tree','Mt Denali','Hawk','Infrared Radiation','Copper','Bhaskara II','Germany','Australian Euro','Neil Armstrong','Yangtze','Eagle','12']

optC_easy = ['Camel','Rabindranath Tagore','Neptune','Apple Tree','Mt Lucania','Eagle','X-Rays and Gamma Rays','Zinc','Vikram Sarabhai','Italy','Australian Mark','Buzz Aldrin','Nile','Emu','8']

optD_easy = ['Elephant','Sarojini Naidu','Jupiter','Banyan Tree','Mt Bona','Vulture','UV Radiation','Lead','Albert Einstein','Hungary','Australian Pound','Yuri Gagarin','Amazon','Ostrich','14']

optA_med = ['Hubble Telescope','Afghans','Japan','Kalpana Chawla','1944','Human Behaviour','USA','26m x 14m','Cricket','Earthquake','Protozoa','Cairo','Pune','1958 in Tokyo','1950']

optB_med = ['Chandra X-Ray Observatory','Rajputs','China','Valentina Tereshkova','1914','Insects','India','28m x 15m','Football','Rainfall','Virus','Addis Ababa','Mumbai','1962 in Jakarta','1948']

optC_med = ['James Webb Telescope','Mughals','New Zealand','Sally Ride','1916','Origin of Words','UK','27 m x 16 m','Hockey','Ocean Depth','Bacteria','Nairobi','Kolkata','1966 in Bangkok','1956']

optD_med = ['Spitzer Space Telescope','The British','Cambodia','Sunita Williams','1940','Formation of Rocks','Fiji','28 m x 16 m','Volleyball','Sound Intensity','Mosquito','Dodoma','Hyderabad','1970 in Bangkok','1952']

optA_hard = ['Femur','Charles Babbage','William Jones',"Lord's",'Kajita Takaaki','1099 AD','May 18','19 January 1918','Vice-Admiral R.D. Katari','2002']

optB_hard = ['The Stapes','Peter Henlein','John Marshall','Old Trafford','Barry C. Barish','1200 AD','June 8','30 May 1918','Gen. K.M. Cariappa','2001']

optC_hard = ['Ulna','Sir Isaac Newton','Alexandar Cunningham','The Oval','Kip Thorne','1515 AD','June 18','11 November 1918','Gen. Maharaja Rajendra Singhji','2000']

optD_hard = ['Coccyx','Micheal Faraday','Charles Wilkins','Trent Bridge','Roger Penrose','1000 AD','May 8','15 February 1918','General Bikram Singh','2003']

# Flip Options List

optA_flip = ['Dadabhai Naoroji','September 11, 2000','1974','4','18 yards']

optB_flip = ['Bal Gangadhar Tilak','September 11, 2001','1978','5','20 yards']

optC_flip = ['Bipin Chandra Pal','September 26, 2001','1984','11','22 yards']

optD_flip = ['C Vijaraghavachari','September 26, 2000','1972','7','24 yards']

# Correct answer list

optA_easy_ans = [' ','Pingali Venkayya',' ',' ',' ',' ',' ',' ','Aryabhatta',' ','Australian Dollar',' ',' ',' ','10']

optB_easy_ans = [' ',' ',' ',' ','Mt Denali',' ',' ',' ',' ',' ',' ','Neil Armstrong',' ',' ',' ']

optC_easy_ans = ['Camel',' ',' ',' ',' ',' ',' ','Zinc',' ','Italy',' ',' ','Nile',' ',' ']

optD_easy_ans = [' ',' ','Jupiter','Banyan Tree',' ','Vulture','UV Radiation',' ',' ',' ',' ',' ',' ','Ostrich',' ']

optA_med_ans = [' ','Afghans','Japan',' ',' ',' ',' ',' ',' ','Earthquake',' ',' ','Pune','1958 in Tokyo',' ']

optB_med_ans = [' ',' ',' ','Valentina Tereshkova',' ','Insects',' ','28m x 15m','Football',' ',' ',' ',' ',' ',' ']

optC_med_ans = ['James Webb Telescope',' ',' ',' ','1916',' ',' ',' ',' ',' ',' ','Nairobi',' ',' ',' ']

optD_med_ans = [' ',' ',' ',' ',' ',' ','Fiji',' ',' ',' ','Mosquito',' ',' ',' ','1952']

optA_hard_ans = [' ',' ',' ',' ',' ','1099 AD',' ',' ',' ','2002']

optB_hard_ans = ['The Stapes','Peter Henlein',' ',' ',' ',' ',' ',' ','Gen. K.M. Cariappa',' ']

optC_hard_ans = [' ',' ',' ','The Oval','Kip Thorne',' ',' ','11 November 1918',' ',' ']

optD_hard_ans = [' ',' ','Charles Wilkins',' ',' ',' ','May 8',' ',' ',' ']

# Correct answer list for flipped question

optA_flip_ans = [' ',' ',' ',' ',' ']

optB_flip_ans = [' ','September 11, 2001',' ','5',' ']

optC_flip_ans = [' ',' ','1984',' ','22 yards']

optD_flip_ans = ['C Vijaraghavachari',' ',' ',' ',' ']

# Correct percentage of answers for audience poll

audienceOptA_easy = [5,75,2,12,7,17,16,10,73,9,70,28,3,13,85]

audienceOptB_easy = [3,3,10,15,63,10,18,12,17,13,10,57,5,9,6]

audienceOptC_easy = [90,7,4,8,20,7,15,69,8,54,6,5,75,17,7]

audienceOptD_easy = [2,15,80,65,10,66,51,9,2,24,14,10,17,61,2]

audienceOptA_med = [22,57,66,16,3,6,8,13,11,68,12,19,74,52,28]

audienceOptB_med = [4,3,7,53,21,73,20,57,67,18,11,20,7,32,4]

audienceOptC_med = [62,30,20,13,66,10,5,5,14,8,21,51,10,13,8]

audienceOptD_med = [12,10,7,18,10,11,67,25,8,6,56,10,9,3,60]

audienceOptA_hard = [11,12,17,16,23,52,6,22,17,56]

audienceOptB_hard = [55,58,10,14,11,15,17,12,61,18]

audienceOptC_hard = [11,17,13,54,59,18,14,53,11,12]

audienceOptD_hard = [23,13,60,16,7,15,63,13,11,14]

# Correct percentage of answers for audience poll for flipped question

audienceOptA_flip = [7,17,18,19,1]

audienceOptB_flip = [11,65,12,67,2]

audienceOptC_flip = [18,7,54,6,82]

audienceOptD_flip = [64,11,16,8,15]

# Amount list

amount_won = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000,0]