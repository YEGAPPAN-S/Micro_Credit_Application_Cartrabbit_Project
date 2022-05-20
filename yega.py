import streamlit as st                                             #import streamlit library for create best machine learning application
import pandas as pd                                                #import pandas library for data frame work
from PIL import Image                                              #import image library from PIL for add image
import mysql.connector as sql                                      #import mysql library for data base connection and save data
conn=sql.connect(host="localhost",user="root",passwd="",database="bank_loan_db")  #call sql data base using mysql library
                                                                   #create insert() function for insert data in database
def insert(email,number,fn,ad,pan,com,csal,psal,house,rent,exp,emi,emi_amt,pdate,edate,bank,duration,eligible,loan_giv,loan_emi):
    res=conn.cursor()                                              #communicate with sql database
    sql="insert into users (EMAIL_ID,MOBILE_NO,NAME,ADDRESS,PAN,COMPANY_NAME,CURRENT_SALARY,PREVIOUS_SALARY,HOUSE,RENT,EXPENSE,TOTAL_EMI,TOTAL_EMI_AMOUNT,PREVIOUS_HIKE_DATE,ESTIMATE_HIKE_DATE,BANK_NAME,LOAN_DURING,ELIGIBLITY,Eligible_Amount,One_Month_EMI) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"     #sql comment line for insert data
    users=(email,number,fn,ad,pan,com,csal,psal,house,rent,exp,emi,emi_amt,pdate,edate,bank,duration,eligible,loan_giv,loan_emi)
    res.execute(sql,users)                                         #execute the query
    conn.commit()                                                  #used for committing

def run():                                                         #create run() function for user page
    st.subheader("Registration")                                   #give subheader for user page
    email = st.text_input("Email Id*")                             #get E-mail detail from user
    number = st.text_input("Mobile Number*",max_chars=10)          #get mobile number detail from user
       
    if st.button("Register"):                                      #give register button for check
        if(email=="" or number==""):                               #check the field is filled or empty
            st.warning("Please Fill All Fields")                   #show warning if the field is empty
        else:
            st.success("You Have To Fill The Loan Form")           #show fill the form if the field is fill
    st.title("Bank Loan Form")                                     #add title
    fn = st.text_input('Full Name*')                               #get full name from user
    ad = st.text_input('Address*')                                 #get address detail from user
    pan = st.text_input("PAN Number*",max_chars=10)                #get pan detail from user with maximum character 10
    com= st.text_input('Company Name*')                            #get company detail from user
    csal = st.number_input("Current Salary Per Month*",value=0)    #get current salary detail from user
    psal = st.number_input("Previous Salary Per Month*",value=0)   #get previous salary detail from user
    house = st.radio("House*",('Own House','Rental House'))        #get house detail from user by ratio button
    rent=0                                                         #assign the house rent value=0 if own house
    if house!="Own House":                                         #get house rent detail from user                                    
        rent= st.number_input("House Rent Amount*",value=0)
    
    
    st.write("Monthly Expense*(Choose The Field and Enter Your Amount)")      #get monthly expense detail from user
    shop=0
    shopping= st.checkbox("Shopping")                                         #get shopping detail from user
    if shopping:
        shop=st.number_input("How Much Will You Spent For Shopping in a Month ?(Including Clothing,Grocery's,Restaurant's,etc...)",value=0)
    cine=0
    cinema= st.checkbox("Cinema")                                             #get cinema amount detail from user
    if cinema:
        cine=st.number_input("How Much Will You Spent For Cinema in a Month ?",value=0)
    online=0
    Oshop= st.checkbox("Online Shopping")                                     #get online shopping detail from user
    if Oshop:
        online=st.number_input("How Much Will You Spent For Online Shopping in a Month ?",value=0)
    park=0
    beach= st.checkbox("Entertainment")                                       #get entertainment amount detail from user
    if beach:
        park=st.number_input("How Much Will You Spent For Park and Beach in a Month ?",value=0)
    tran=0
    transp= st.checkbox("Transport")                                          #get transport detail from user
    if transp:
        tran=st.number_input("How Often Will You Spend For Transport in a Month ?",value=0)
    heal=0
    health= st.checkbox("Health")                                             #get health detail from user
    if health:
        heal=st.number_input("How Often Will You Spent For Doctor CheckUp in a Month ?(If Any Health Issues)",value=0)
    othexp=0
    otherexpence = st.checkbox("Other Expence")                               #get other expense detail from user
    if otherexpence:
        othexp=st.number_input("How Much Will You Spent For Other Things ",value=0)
    exp=shop+cine+online+park+tran+heal+othexp                                #add all expense amount
        
    emi= st.slider("Total Number Of EMI's*", 0, 10)                           #get total emi's detail from user
    emi_amt =0                                                                #assign the emi value=0 if no emi
    if emi!=0:
        emi_amt = st.number_input("Total EMI Amount Per Month*",value=0)      #get emi amount detail from user
    pdate=st.date_input('Previous Hike Date')                                 #get previous hike date detail from user
    edate=st.date_input('Estimate Hike Date')                                 #get estimate hike date detail from user
    bank = st.selectbox("Bank Name*",('STATE BANK OF INDIA','INDIAN OVERSEAS BANK','KARUR VYSYA BANK','CITY UNION BANK','ICICI BANK','Other Banks'))                                                                               #get bank name from user by select box
    if bank=="Other Banks":
         bank= st.text_input("Bank Name*")                                             #get bank name from user if bank name not in the list
    dur_display = ['2 Month','6 Month','8 Month','1 Year','16 Month','None Of These']  #get loan duration detail from user by select box
    dur_options = range(len(dur_display))
    dur = st.selectbox("Loan Duration*",dur_options, format_func=lambda x: dur_display[x])
    if dur==5:
        dur1 = st.number_input("Please Enter Your Duration Month (Enter The Value in Month's)*",value=0) #get loan duration detail from user if the duration month not in the list
    if st.button("Submit"):                                                    #give submit button
        if(fn=="" or ad=="" or pan=="" or com=="" or csal==0 or psal==0 or email=="" or number==""): #check all fields are filled or not
                st.warning("Please Fill All Fields")                           #show warning if the field is empty
        else:
                if dur == 0:                                                   #assign value for duration 2 if select 0'th index
                    duration = 2
                if dur == 1:                                                   #assign value for duration 6 if select 1'th index
                    duration = 6
                if dur == 2:                                                   #assign value for duration 8 if select 2'nd index
                    duration = 8                                               
                if dur == 3:                                                   #assign value for duration 12 if select 3'rd index
                    duration = 12
                if dur == 4:                                                   #assign value for duration 16 if select 4'th index
                    duration = 16
                if dur == 5:                                                   #get value for duration if select 5'th index
                    duration = dur1
                
                loan_giv=((csal-rent-emi_amt-exp)*duration)*50/100             #calculate loan amount
                loan_emi=loan_giv/duration                                     #calculate emi amount
        
                if (loan_giv<loan_emi):                                        #check eligible or not
                    eligible="NOT ELIGIBLE"
                    st.error("Sorry " + fn +' According to our Calculations, you will not get the loan from our Bank') #print not eligible
                    #insert data using insert() function
                    insert(email,number,fn,ad,pan,com,csal,psal,house,rent,exp,emi,emi_amt,pdate,edate,bank,duration,eligible,"0","0") 
                else:
                    eligible="ELIGIBLE"
                    st.success("Hello  " + fn +' Congratulations!! you will get the loan from our Bank')          #print eligible
                    st.write("Your Eligible Amount is", loan_giv )                                                #print eligible amount
                    st.write("Your Repayment period is ", duration,"months")
                    st.write("Your One Month EMI is", loan_emi )                                                  #print emi amount
                    insert(email,number,fn,ad,pan,com,csal,psal,house,rent,exp,emi,emi_amt,pdate,edate,bank,duration,eligible,loan_giv,loan_emi)  #insert data

def main():                                                       #create main() function for admin page
    img1 = Image.open('cartrabbit.png')                           #call image using image library
    img1 = img1.resize((156,145))                                 #resize image
    st.image(img1,use_column_width=False)                         #add image

    st.title("Cartrabbit's Bank Loan")                            #add title 

    menu = ["User Registration","Admin Login"]                    #create menu
    choice = st.sidebar.selectbox("Menu",menu)                    #create sidebar for menu option


    if choice == "Admin Login":                                   #admin page
        st.subheader("Admin Login")                               #header
        User_Name = st.text_input("User Name")                    #get user name from admin
        Password = st.text_input("Password",type="password")      #get password from admin
        if(User_Name=="yegappan" and Password=="yega@342"):       #validate user name and password
            if st.button("Show Database"):                        #show data base button
                st.button("Hide Database")                        #hide data base button
                res=conn.cursor()                                 #communicate with sql database
                sql="SELECT EMAIL_ID,MOBILE_NO,NAME,ADDRESS,PAN,COMPANY_NAME,CURRENT_SALARY,PREVIOUS_SALARY,HOUSE,RENT,EXPENSE,TOTAL_EMI,TOTAL_EMI_AMOUNT,PREVIOUS_HIKE_DATE,ESTIMATE_HIKE_DATE,BANK_NAME,LOAN_DURING,ELIGIBLITY,Eligible_Amount,One_Month_EMI from users"   #sql comment for select and show data
                res.execute(sql)                                   #execute the query
                result=res.fetchall()                              #select all data from database
                db = pd.DataFrame(result,columns=["EMAIL_ID","MOBILE_NO","NAME","ADDRESS","PAN","COMPANY_NAME","CURRENT_SALARY","PREVIOUS_SALARY","HOUSE","RENT","EXPENSE","TOTAL_EMI","TOTAL_EMI_AMOUNT","PREVIOUS_HIKE_DATE","ESTIMATE_HIKE_DATE","BANK_NAME","LOAN_DURING","ELIGIBLITY","Eligible_Amount","One_Month_EMI"])
                st.dataframe(db)                                  #print database in dataframe using pandas
            
        else:
            if st.button("Show Database"):                        #show database button
                st.warning("Please Enter The Valid Password")     #print error message when the password become wrong
 
    elif choice == "User Registration":                           #go to registration form
                run()                                             #run run() function
main()                                                            #run main() function
