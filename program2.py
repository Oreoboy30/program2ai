import streamlit as st


if 'result' not in st.session_state:
        
    ST_max = [5000, 10000, 7500, 8500, 9500]
    ST_CR = [[20, 15, 10, 21, 5], [30, 16, 15, 10, 2], [22, 15, 11, 12, 3],[16, 16, 16, 15, 1], [19, 10, 20, 15, 1]]
    ST_vac = [[15000, 434890, 115900], [35234,378860,100450], [22318,643320,223400], [23893,859900,269300], [19284,450500,221100]]
    CR = [[200,100],[500,250],[1000,500],[2500,800],[4000,1200]]
    ST_name = ["ST-1", "ST-2", "ST-3", "ST-4", "ST-5"]
    final_result=[[],[],[],[],[]]
    result_array = [[5000,0,0,0,2,0,1600,790,4,0,0,0,0,400,3,4,90,90,114,1600,113,400,181200],
    [10000,0,0,0,1,2,3200,4544,3,0,0,0,1,1500,4,4,42,42,52,3200,51,1500,164700],
    [7500,0,0,0,0,2,2400,4038,1,0,0,0,1,1300,3,3,89,89,119,2400,118,1300,284500],
    [8500,0,0,0,2,1,2800,5593,3,0,0,2,0,1900,3,3,104,104,136,2800,135,1900,379900],
    [9500,0,1,0,2,1,3050,6884,2,0,0,1,1,2200,3,3,50,50,73,3050,72,2200,221800]]
    
    for i in range(5):

        result1 = "ST-" + str(i+1) + ":" 
        result2 = "  Max Day: " + str(result_array[i][0])
        result3 = """  CR-1: {0:d}, CR-2: {1:d}, CR-3: {2:d}, CR-4: {3:d}, CR-5: {4:d}""".format(
                    result_array[i][1], result_array[i][2], result_array[i][3], result_array[i][4], result_array[i][5])
        result4 = "  Price: RM" + str(result_array[i][6])
        result5 = "  Last Day: " + str(result_array[i][7])
        result6 = """  CR-1: {0:d}, CR-2: {1:d}, CR-3: {2:d}, CR-4: {3:d}, CR-5: {4:d}""".format(
                    result_array[i][8], result_array[i][9], result_array[i][10], result_array[i][11], result_array[i][12])
        result7 = "  Price: RM" + str(result_array[i][13])
        print()
        result8 = """  Vac A: Day 1 - {0:d}, Vac B: Day {1:d} - {2:d}, Vac C: Day {3:d} - {4:d}""".format(
            result_array[i][14], result_array[i][15], result_array[i][16], result_array[i][17], result_array[i][18])
        print()

        result9 = """  Total Price: RM{0:d} * {1:d} + RM{2:d} = RM{3:d}""".format(
            result_array[i][19], result_array[i][20], result_array[i][21], result_array[i][22])

        final_result[i].append(result1)
        final_result[i].append(result2)
        final_result[i].append(result3)
        final_result[i].append(result4)
        final_result[i].append(result5)
        final_result[i].append(result6)
        final_result[i].append(result7)
        final_result[i].append(result8)
        final_result[i].append(result9)
    st.session_state.result = final_result

def totalResult():
    statenum = 0
    state_Name = st.session_state.box
    if state_Name == "ST-1":
        statenum = 0
    elif (state_Name == "ST-2"):
        statenum = 1
    elif (state_Name == "ST-3"):
        statenum = 2
    elif (state_Name == "ST-4"):
        statenum = 3
    elif (state_Name == "ST-5"):
        statenum = 4
    for i in range(9):
        st.text(st.session_state.result[statenum][i])
st.sidebar.selectbox("Choose state",
    ("ST-1", "ST-2", "ST-3", "ST-4", "ST-5"), key="box", on_change=totalResult)