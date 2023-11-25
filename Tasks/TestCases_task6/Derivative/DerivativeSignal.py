def DerivativeSignal():
    # InputSignal=[1f, 2f, 3f, 4f, 5f, 6f, 7f, 8f, 9f, 10f, 11f, 12f, 13f, 14f, 15f, 16f, 17f, 18f, 19f, 20f, 21f, 22f, 23f, 24f, 25f, 26f, 27f, 28f, 29f, 30f, 31f, 32f, 33f, 34f, 35f, 36f, 37f, 38f, 39f, 40f, 41f, 42f, 43f, 44f, 45f, 46f, 47f, 48f, 49f, 50f, 51f, 52f, 53f, 54f, 55f, 56f, 57f, 58f, 59f, 60f, 61f, 62f, 63f, 64f, 65f, 66f, 67f, 68f, 69f, 70f, 71f, 72f, 73f, 74f, 75f, 76f, 77f, 78f, 79f, 80f, 81f, 82f, 83f, 84f, 85f, 86f, 87f, 88f, 89f, 90f, 91f, 92f, 93f, 94f, 95f, 96f, 97f, 98f, 99f, 100f]  
    InputSignal = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 
               17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0, 30.0, 31.0,
               32.0, 33.0, 34.0, 35.0, 36.0, 37.0, 38.0, 39.0, 40.0, 41.0, 42.0, 43.0, 44.0, 45.0, 46.0, 47.0,
               48.0, 49.0, 50.0, 51.0, 52.0, 53.0, 54.0, 55.0, 56.0, 57.0, 58.0, 59.0, 60.0, 61.0, 62.0, 63.0,
               64.0, 65.0, 66.0, 67.0, 68.0, 69.0, 70.0, 71.0, 72.0, 73.0, 74.0, 75.0, 76.0, 77.0, 78.0, 79.0,
               80.0, 81.0, 82.0, 83.0, 84.0, 85.0, 86.0, 87.0, 88.0, 89.0, 90.0, 91.0, 92.0, 93.0, 94.0, 95.0,
               96.0, 97.0, 98.0, 99.0, 100.0]

    expectedOutput_first = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    expectedOutput_second = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    """
    Write your Code here:
    Start
    """
   # Calculate the first derivative using forward difference
    FirstDrev = []
    for i in range(len(InputSignal) - 1):
        derivative = InputSignal[i + 1] - InputSignal[i]
        FirstDrev.append(derivative)

    # Append the last element with the same value as the previous element for compatibility
    FirstDrev.append(FirstDrev[-1])

    # Calculate the second derivative using central difference
    SecondDrev = []
    for i in range(1, len(InputSignal) - 1):
        derivative = InputSignal[i + 1] - 2 * InputSignal[i] + InputSignal[i - 1]
        SecondDrev.append(derivative)

    # Append the first and last elements with the same value as their adjacent elements for compatibility
    SecondDrev = [SecondDrev[0]] + SecondDrev + [SecondDrev[-1]]
    
    
    
    
    """
    End
    """
    
    """
    Testing your Code
    """
    if( (len(FirstDrev)!=len(expectedOutput_first)) or (len(SecondDrev)!=len(expectedOutput_second))):
        print("mismatch in length") 
        return
    first=second=True
    for i in range(len(expectedOutput_first)):
        if abs(FirstDrev[i] - expectedOutput_first[i]) < 0.01:
            continue
        else:
            first=False
            print("1st derivative wrong")
            return
    for i in range(len(expectedOutput_second)):
        if abs(SecondDrev[i] - expectedOutput_second[i]) < 0.01:
            continue
        else:
            second=False
            print("2nd derivative wrong") 
            return
    if(first and second):
        print("Derivative Test case passed successfully")
    else:
        print("Derivative Test case failed")
    return