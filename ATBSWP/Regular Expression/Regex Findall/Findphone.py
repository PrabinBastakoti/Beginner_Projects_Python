
import pprint
import re
message = '''
 Contact Us  Post a Complain  Subordinate offices  Telephone Directory नेपाली  English
  Invert Color A- A A+
Government of Nepal Logo
Nepal Government
Ministry of Home Affairs
Search
   
Home
 
About Us
 
Organization Structure
 
Resources
 
Foreign Tours
 
Progress Report
 
Contact Us
 
FAQ
Telephone Directory
 Telephone Directory
Subordinate offices
Telephone Directory
See offices on the map

Province :
All
Office Type :
All
Office :
All
Designation :
All
Search Keyword :
   
Total Results : 124
S.No	Name	Office	Designation	Division / Section	Phone	Mobile	Email
1	Bal Krishna Khand	Ministry of Home Affairs	Hon'ble Home Minister	N/A			
2	Tek Narayan Pandey	Ministry of Home Affairs	Home Secretary	N/A		9851140001	secretary@moha.gov.np
3	Shiva Ram Pokhrel	Ministry of Home Affairs	Joint Secretary	Internal Management Division	01-4211263	9851140004	management@moha.gov.np
4	Fanindra Mani Pokharel	Ministry of Home Affairs	Joint Secretary	Security and Coordination Division		9851140003	info@moha.gov.np
5	Pradip Kumar Koirala	Ministry of Home Affairs	Joint Secretary	Disaster and Conflict Management Division	01-4211217	9851140005	
6	Dr. Bhishma Kumar Bhusal	Ministry of Home Affairs	Joint Secretary	Policy, Plan, Monitoring and Evaluation Division		9851140011	pppd@moha.gov.np
7	Komal Bahadur Khatri	Ministry of Home Affairs	Joint Secretary	Legal Division		9851140012	
8	TEK Bahadur K.C.	Ministry of Home Affairs	Joint Secretary	Administration Division		9851140002	kctekbdr22@gmail.com
9	Ganesh Gaire	Ministry of Home Affairs	Under Secretary	Police Administration Section	01-4211223	9858750757	ggaire4@gmail.com
10	Rama Acharya (Subedi)	Ministry of Home Affairs	Under Secretary	Disaster and Conflict Management Division	01-4211271	9841558010	acharyasrama4@gmail.com
11	Shobhakhar Regmi	Ministry of Home Affairs	Under Secretary	Personnel Administration Section	4211220	9851152964	rshobhakhar@gmail.com
12	Lila Kumari K.C.	Ministry of Home Affairs	Under Secretary	Citizenship and NID managemnt Section	01-4211239	9843524561	
13	Tulsi Prasad Dahal	Ministry of Home Affairs	Under Secretary	Disaster Study Risk Reduction and Recovery Section	4211200	9851183695	tulsi.dahal@nepal.gov.np
14	GOMADEVI CHEMJONG	Ministry of Home Affairs	Under Secretary	Border and Immigration Administration Section	01-4211276	9851215979	gomadevi.chemjong@moha.gov.np
15	Bishwamitra Kuinkel	Ministry of Home Affairs	Under Secretary	Bibhushan Section	014211261	9851219739	bkuinkel@nepal.gov.np
16	Suresh Sunar	Ministry of Home Affairs	Under Secretary	Peace Promotion Section		9843440040	
17	Krishna Poudel	Ministry of Home Affairs	Under Secretary	Central Haj Committee	+977-1-422385	9843525489	
18	Janak Raj Panta	Ministry of Home Affairs	Under Secretary	N/A		9851138881	
19	Matrika Acharya	Ministry of Home Affairs	Under Secretary	Disaster Preparedness and Response Section (NEOC)	014211262	9851037196	matrika.acharya@nepal.gov.np
20	Khumkanta Acharya	Ministry of Home Affairs	Under Secretary	Grievance Handling Section		9851096139	
21	Gokarna Prasad Upadhyay	Ministry of Home Affairs	Under Secretary	Drug Control Section	+977-1-4211237	9851327222	gpupadhyay@gmail.com
22	Shekhar poudel	Ministry of Home Affairs	Under Secretary	Local Administration and Province Co-Ordination Section		9851092033	Shakhar.poudel@gmail.com
23	Bhimkanta Sharma	Ministry of Home Affairs	Under Secretary	Office Management and Goods Section	01-4211264	9849555500	bhimpandel77@gmail.com
24	Bishworaj Neupane	Ministry of Home Affairs	Under Secretary	Internal Administration, Vechical, Meeting and Ceremony Managemnt Section	01-4200002	9851166778	nrbisu@yahoo.com1
25	Bandana Rai	Ministry of Home Affairs	Under Secretary	N/A		9861599003	rai_bandana5@yahoo.com
26	Ram Datta Pandey	Ministry of Home Affairs	Under Secretary	Human Rights Promotion Section	01-4211186	9841554121	pandey_111@yahoo.com
27	Arjun Poudel	Ministry of Home Affairs	Under Secretary	Planing, Monitoring and Evaluation Section	01-4211262	9851165368	
28	Basanta Bhattarai	Ministry of Home Affairs	Under Secretary	Peace, Security and Crime Control Section		9851277012	informationofficer@moha.gov.np
29	Sushma Shrestha	Ministry of Home Affairs	Senior Computer Engineer	Information & Technology Section	014211252	9841821257	sushma.shrestha@nepal.gov.np
30	Mohan Sharan Bhandri	Ministry of Home Affairs	Under Secretary (Account)	Account Section		9847037314	bhandaryms@gmail.com
31	Kabita Sharma	Ministry of Home Affairs	Section Officer	Police Administration Section	14211200	9849594100	sharmakabita11@gmail.com
32	BISHNU PRASAD ARCHYA	Ministry of Home Affairs	Section Officer	Secretariat of Home Minister		9851065579	bishnuanacharya@gmail.com
33	Saraswati Sapkota	Ministry of Home Affairs	Section Officer	Disaster Study Risk Reduction and Recovery Section		9849631909	sapkotasaru01@gmail.com
34	Ranjana Rai	Ministry of Home Affairs	Section Officer	Disaster Study Risk Reduction and Recovery Section	9851277011	9845288924	ranjana_rai88@yahoo.com
35	Rajendra Prasad Gautam	Ministry of Home Affairs	Section Officer	Border and Immigration Administration Section	014211274	9841551351	rgtm888@gmail.com
36	Narayan Khatri	Ministry of Home Affairs	Section Officer	Peace Promotion Section		9857066977	
37	Deepak Prasad Neupane	Ministry of Home Affairs	Section Officer	Disaster Study Risk Reduction and Recovery Section	4211281	9851213515	dipak_neupane@hotmail.com
38	Muskan Kumar Maskey	Ministry of Home Affairs	Section Officer	Office Management and Goods Section		9841391921	muskankr21@gmail.com
39	Rembu Chamling Rai	Ministry of Home Affairs	Section Officer	Grievance Handling Section	01-4200634	9808017111	rembu.rai@nepal.gov.np
40	Sahanshila Pudasaini	Ministry of Home Affairs	Section Officer	Legal Decision Administration Section		9849744218	pudasaini.sahanshila@yahoo.com
41	Bijya Raj Poudel	Ministry of Home Affairs	Section Officer	Citizenship and NID managemnt Section	01-4211245	9851243465	rbpoudel53@gmail.com
42	Jagdish Aryal	Ministry of Home Affairs	Section Officer	Border and Immigration Administration Section	014211274	9851001441	jagaryal@gmail.com
43	Pratikshya K.C.	Ministry of Home Affairs	Section Officer	Legal Decision Administration Section	01-4211268	9841895990	
44	Antosh Pradhan	Ministry of Home Affairs	Section Officer	Local Administration and Province Co-Ordination Section	01-4211266	9840648564	anty.pradhan@gmail.com
45	Kiran Chandra Subedi	Ministry of Home Affairs	Section Officer	Drug Control Section		9840600888	kirancsubedi@gmail.com
46	Sangita Koirala	Ministry of Home Affairs	Section Officer	Border and Immigration Administration Section	01-4211210		
47	कुलशेखर अर्याल	Ministry of Home Affairs	Section Officer	Personnel Administration Section		9851225880	aryalks@gmail.com
48	Bhashkar Dhahal	Ministry of Home Affairs	Section Officer	Personnel Administration Section		9841347559	
49	Dinesh Neupane	Ministry of Home Affairs	Section Officer	Peace, Security and Crime Control Section	4211208		
50	Khemraj Sapkota	Ministry of Home Affairs	Section Officer	Grievance Handling Section		9845148601	khemrajsapkota601@gmail.com
51	Narbada Ghimire	Ministry of Home Affairs	Section Officer	Local Administration and Province Co-Ordination Section	4211266	9849772652	narbada.moha2076@gmail.com
52	Ramesh Rijal	Ministry of Home Affairs	Section Officer	Disaster Preparedness and Response Section (NEOC)			
53	Anilraj Koirala	Ministry of Home Affairs	Section Officer	Human Rights Promotion Section		9856021357	anilkoirala05@gmail.com
54	Hari Prasad Dahal	Ministry of Home Affairs	Section Officer	Secretariat of Secretary MOHA	01-4211249		
55	Laxmi Marasini	Ministry of Home Affairs	Section Officer	Planing, Monitoring and Evaluation Section	+977-1-4211262	9847105835	lachhu.marasini3@gamil.com
56	Narendra Pariyar	Ministry of Home Affairs	Section Officer	Planing, Monitoring and Evaluation Section	+977-1-4211262	9841400535	nppyarelal@gmail.com
57	Ashok Kumar Acharya	Ministry of Home Affairs	Section Officer	Citizenship and NID managemnt Section	01-4211245		
58	Laxmikumari Shahi	Ministry of Home Affairs	Section Officer	Drug Control Section			
59	Sharadha Chalise	Ministry of Home Affairs	Section Officer	Peace Promotion Section		9849034051	saradhachalise051@gmail.com
60	Sarmila Banjande	Ministry of Home Affairs	Section Officer	Relief and Data Management Section			
61	Bishnubhaka Sigdel	Ministry of Home Affairs	Section Officer	Relief and Data Management Section			
62	Gopal Shrestha	Ministry of Home Affairs	Section Officer	Office Management and Goods Section	01-4211253	9849108490	
63	Smarat Thapa Magar	Ministry of Home Affairs	Section Officer	Peace, Security and Crime Control Section		0014211208	
64	kula Raj Subedi	Ministry of Home Affairs	Section Officer	Planing, Monitoring and Evaluation Section		9841371573	kularajsubedi@gmail.com
65	Suman Pandit	Ministry of Home Affairs	Section Officer	Peace, Security and Crime Control Section	+977-1-4211214	9851127999	pandit.suman@gmail.com
66	Sanjaya Kumar Pokhrel	Ministry of Home Affairs	Section Officer	Peace, Security and Crime Control Section			
67	Tulshi Bhattarai	Ministry of Home Affairs	Section Officer	Peace, Security and Crime Control Section		9851165962	tulshibhattarai2068@gmail.com
68	Bishnu Hari Timalsena	Ministry of Home Affairs	Section Officer	Peace, Security and Crime Control Section		9841456820	btjbishnulaxmi708@gmail.com
69	Shalikram Parajuli	Ministry of Home Affairs	Account Officer	Account Section		9841825560	shalik_2006@yahoo.com
70	Prabhat Subash Kharel	Ministry of Home Affairs	Computer Engineer	Information & Technology Section	01-4211204		subkha3@gmail.com
71	Diwos Karki	Ministry of Home Affairs	Computer Engineer	Information & Technology Section	01-4211171		diwos.karki@moha.gov.np
72	Bishwas Pokharel	Ministry of Home Affairs	Computer Engineer	Information & Technology Section	01-4211171		bishwas.pokharel@moha.gov.np
73	Prabhat Kumar Mallik	Ministry of Home Affairs	Computer Operator	Information & Technology Section	4211204		shubhprabhat50@gmail.com
74	Rabindra Singh	Ministry of Home Affairs	Computer Operator	Disaster Study Risk Reduction and Recovery Section			
75	Umesh Neupane	Ministry of Home Affairs	Computer Operator	Account Section	4211278	9841439835	umesh_neupane@hotmail.com
76	Lalit Singh Karki	Ministry of Home Affairs	Computer Operator	Peace, Security and Crime Control Section	4211208	9868403342	karkilalitsingh@yahoo.com
77	Muna Neupane	Ministry of Home Affairs	Computer Operator	Personnel Administration Section	4211270	9846802141	muna.neupane@moha.gov.np
78	Binod Biswokarma	Ministry of Home Affairs	Computer Operator	Peace, Security and Crime Control Section	4211208	9843938002	bikalpbinod@gmail.com
79	KABINA NAPIT	Ministry of Home Affairs	Computer Operator	Grievance Handling Section		9841174606	napitkabina8@gmail.com
80	Sapana Thapa Magar	Ministry of Home Affairs	Computer Operator	Relief and Data Management Section			dreamydreamerr2018@gmail.com
81	Pradeep Kumar Yadav	Ministry of Home Affairs	Computer Operator	Planing, Monitoring and Evaluation Section		9845313468	pradeepyadavbrj82@gmail.com
82	Raj Kumar Chaudhary	Ministry of Home Affairs	Computer Operator	Information & Technology Section	4211204		rajkumar@moha.gov.np
83	Dhanraj Budha	Ministry of Home Affairs	Computer Operator	Peace, Security and Crime Control Section		9864877476	dhanrajbudha75@gmail.com
84	Prakesh Bahadur Khati	Ministry of Home Affairs	Computer Operator	Secretariat of Home Minister			
85	Sabita Dhakal	Ministry of Home Affairs	Computer Operator	Internal Administration, Vechical, Meeting and Ceremony Managemnt Section		9849990771	sabitadbakal075@gmail.com
86	Deep Sagar Dangi	Ministry of Home Affairs	Computer Operator	Registration Section		9869875847	sagardangi@gmail.com
87	Pawan gurung	Ministry of Home Affairs	Computer Operator	Internal Administration, Vechical, Meeting and Ceremony Managemnt Section		9862032211	xcuhaepawan@gmail.com
88	Yamuna K. C.	Ministry of Home Affairs	Computer Operator	Disaster Study Risk Reduction and Recovery Section		9847993334	yamunakc53@gmail.com
89	Bibek Mishra	Ministry of Home Affairs	Computer Operator	Office Management and Goods Section		9865011244	bmloksewa125@gmail.com
90	Shushil kumar singh	Ministry of Home Affairs	Computer Technicial	Office Management and Goods Section	4211255	9849638280	sushil.singh2076@gmail.com
91	Sarita Rai	Ministry of Home Affairs	Nayab Subba	Disaster and Conflict Management Division	01-4211241	९८४३८२१०६१	
92	Abindra K.C.	Ministry of Home Affairs	Nayab Subba	Internal Management Division	+977-1-4211263	9849157942	abindrakc1@gmail.com
93	Sanjeev Dhakal	Ministry of Home Affairs	Nayab Subba	Grievance Handling Section	01-4211261		
94	Bidur Kumar Bhandari	Ministry of Home Affairs	Nayab Subba	Peace, Security and Crime Control Section			
95	Ram Chandra Sharma	Ministry of Home Affairs	Nayab Subba	Peace Promotion Section		9843772298	
96	Anil Ji. Si.	Ministry of Home Affairs	Nayab Subba	Faulty Asset Management Unit		9855041418	anilgc4950@gmail.com
97	Surendra Shing Airi	Ministry of Home Affairs	Nayab Subba	Secretariat of Home Minister		9849033664	
98	Anjali Ramtel	Ministry of Home Affairs	Nayab Subba	Registration Section		9849387877	
99	Umesh Bhatterai	Ministry of Home Affairs	Nayab Subba	Secretariat of Secretary MOHA	01-4211249	9843686732	hseumbht@gmail.com
100	Shakuntala Subedi	Ministry of Home Affairs	Nayab Subba	Chalani	014211262	9849274977	subedishakuntala13@gmail.com
101	Shyam Krishna Lamichhane	Ministry of Home Affairs	Nayab Subba	Secretariat of Secretary MOHA	01-4211249	9851173434	shyamlamichhane983@gmail.com
102	Nawa Raj Joshi	Ministry of Home Affairs	Nayab Subba	Personnel Administration Section	+977-1-4211254	9848683341	nawaraj.joshi@moha.gov.np
103	Prem Prasad Poudel	Ministry of Home Affairs	Nayab Subba	Local Administration and Province Co-Ordination Section		9857631215	
104	Mahadev Thapa	Ministry of Home Affairs	Nayab Subba	Secretariat of Secretary MOHA		9841770805	
105	Khubraj Shrestha	Ministry of Home Affairs	Nayab Subba	Peace, Security and Crime Control Section	01-4211214		
106	Subit Kumar Sunuwar	Ministry of Home Affairs	Nayab Subba	Peace, Security and Crime Control Section	01-4211214		
107	Kamal Acharya	Ministry of Home Affairs	Nayab Subba	Planing, Monitoring and Evaluation Section		9844818750	kamalnabin@gmail.com
108	Nar Bahadru Kunwar	Ministry of Home Affairs	Accoutannt	Account Section		9860680463	
109	Rupesh Bishwakarma	Ministry of Home Affairs	Accoutannt	Account Section	01-4211278	9855071198	
110	Kanchha Thapa	Ministry of Home Affairs	Accoutannt	Account Section	01-4211278	9823570902	
111	Balram Rimal	Ministry of Home Affairs	Accoutannt	Account Section	01-4211278	9841403953	
112	Jeewan Thapa Magar	Ministry of Home Affairs	Kharidar	Personnel Administration Section	4211270	9841273097	
113	Shisir Bhattarai	Ministry of Home Affairs	Kharidar	Administration Division			beingccr46@gmail.com
114	Kalpana Khadka Basnet	Ministry of Home Affairs	Office Helper	Account Section	4211254	9849559621	
115	Manima Devi KaTharu	Ministry of Home Affairs	Office Helper	Grievance Handling Section	01-4211261		
116	Durga Subedi	Ministry of Home Affairs	Office Helper	Internal Administration, Vechical, Meeting and Ceremony Managemnt Section		9849209684	durgasubedi@gmail.com
117	Shiva Bahadur Basnet	Ministry of Home Affairs	Office Helper	Personnel Administration Section	01-4211270	9843148377	
118	Anita Pandey	Ministry of Home Affairs	Office Helper	Registration Section			
119	Nirmala Parajuli	Ministry of Home Affairs	Office Helper	Administration Division	01-4211204	9841691502	
120	Rama Devi Baniya	Ministry of Home Affairs	Office Helper	Secretariat of Secretary MOHA		9849990240	
121	Kaamana Bhandari	Ministry of Home Affairs	Armed Police Attendant	Peace, Security and Crime Control Section	14211275	9849395805	
122	Bandana Bhujel	Ministry of Home Affairs	Armed Police Attendant	Disaster Preparedness and Response Section (NEOC)	4200203	9849885474	
123	Som Bahadur Tamang	Ministry of Home Affairs	प्रहरी हवल्दार	Disaster Preparedness and Response Section (NEOC)	4200203	9860927286	tamangsom32@yahoo.com
124	दिनेश बस्नेत	Ministry of Home Affairs	सशस्त्र प्रहरी सहायक हवल्दार	Police Administration Section	4200203	9849668658	
Contact
Ministry of Home Affairs
Singhdurbar, Kathmandu

 +977-1-4211208, +977-1-4211214
1112 (Toll Free No.)

 +977-1-4211257, +977-1-4211286

 control@moha.gov.np
gunaso@moha.gov.np

Follow us on
 
Terms of Use | Privacy Policy
Important Links
Nepal Police
Armed Police Force, Nepal
Nepal Disaster Risk Reduction Portal
National Emergency Operation Center
National Library (Police)
Department of National Identity card and Vital Registration
Department of Prison Management
Nepal Immigration
Office Hours
10:00 AM - 5:00 PM (Normal Working Days, Sunday to Thursday)
10:00 AM - 3:00 PM (Friday)

Last Updated : 2079-04-23 17:04:48
© All Rights Reserved to Ministry of Home Affairs

Powered By: ProActive Developers

'''
phonenumberregex = re.compile(r'\d\d\d\d\d\d\d\d\d\d')
mo = phonenumberregex.findall(message)

pprint.pprint(mo)