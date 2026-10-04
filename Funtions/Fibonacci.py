def fibonacci():
    n = int(input("Enter a number and i'll print fibonacci series: "))
    first =0
    sec =1
    count = 0
    while count < n//2:
        #yee loop "n times" run ho ga kylin har loop mein 2 dafa print statement hai 
        #jis ki wajah sy "2n" numbers print hon gy
        #iss liyee ham n ko half kar dyty hain like "n//2"
        #lykin yee odd k cae mein galat ho jai ga
        #iss liyee odd case k liyee if mein ak aur print statement likhny ho gi
        print (first)
        print (sec)
        first = first + sec
        sec = sec + first
        count = count +1
    if n%2 !=0:
        print(first)
    print("Task done...")


fibonacci()