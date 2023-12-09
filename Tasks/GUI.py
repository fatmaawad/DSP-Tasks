from Task1 import *
from Task2 import *
from Task3 import *
from Task4 import*
from Task5 import *
from Task6 import *
from Task7 import *
from Task8 import *
from helper_functions import *
from TEST import*
from TestCases_task6.Shifting_and_Folding.Shift_Fold_Signal import *


    
def show_frame():
    window = tk.Tk()
    window.title('Signal Processing')
    window.geometry("800x800")
    window.configure(bg="#e4c8d4")
    main_frame = tk.ttk.Notebook(window)

    fa = StringVar()
    f = StringVar()
    fs = StringVar()
    fp = StringVar()


        
        
    frame1 = tk.Frame(main_frame, width=400, height=300)
    frame2 = tk.Frame(main_frame, width=400, height=300)
    frame3 = tk.Frame(main_frame, width=400, height=300)
    frame4 = tk.Frame(main_frame, width=400, height=300)
    frame5 = tk.Frame(main_frame, width=400, height=300)
    frame6 = tk.Frame(main_frame, width=400, height=300) 
    
 

    button1 = Button(frame1, width=20, text="Choose File", command=lambda: plot_signal(frame1),
                     font=('arial', 12, 'bold'))
    button1.place(x=700, y=90)
    button1.pack()

    tk.Label(frame2, text="Amplitude:").place(x=200, y=120)
    amplitude_entry = Entry(frame2, textvariable=fa)
    amplitude_entry.place(x=300, y=120)
    amplitude_entry.insert(0, "1.0")

    ttk.Label(frame2, text="Phase Shift (radians):").place(x=170, y=90)
    phase_shift_entry = Entry(frame2, textvariable=fp)
    phase_shift_entry.place(x=300, y=90)
    phase_shift_entry.insert(0, "0.0")

    ttk.Label(frame2, text="Sampling Frequency (Hz):").place(x=170, y=180)
    sampling_frequency_entry = Entry(frame2, textvariable=fs)
    sampling_frequency_entry.place(x=300, y=180)
    sampling_frequency_entry.insert(0, "10.0")

    ttk.Label(frame2, text="Frequency (Hz):").place(x=200, y=150)
    frequency_entry = Entry(frame2, textvariable=f)
    frequency_entry.place(x=300, y=150)
    frequency_entry.insert(0, "1.0")

    signal_type_var = tk.StringVar()
    ttk.Label(frame2, text="Signal Type:").place(x=200, y=210)
    list = ["sine", "cosine"]
    v = StringVar()
    droplist = OptionMenu(frame2, v, *list)
    v.set("Select type")
    droplist.config(width=10)
    droplist.place(x=300, y=605)

    def display_signal():
        amplitude = float(fa.get())
        frequency = float(f.get())
        phase_shift = float(fp.get())
        sampling_frequency = float(fs.get())
        signal_type = v.get()
        signal = generate_signal(signal_type, amplitude, phase_shift, frequency, sampling_frequency)
        display_file_signal(signal, sampling_frequency)
        SignalSamplesAreEqual('SinOutput.txt', '', signal)

    ttk.Button(frame2, text="Generate and Display Signal", command=display_signal).place(x=250, y=250)

    ttk.Label(frame3, text="Select operation:").place(x=200, y=220)
    operations = ["Addition", "Subtraction", "Multiplication", "Squaring", "Shifting", "Normalization", "Accumulation"]
    operation_var = StringVar()
    operation_menu = OptionMenu(frame3, operation_var, *operations)
    operation_var.set("Select operation")
    operation_menu.config(width=10)
    operation_menu.place(x=300, y=210)

    ttk.Label(frame3, text="mult_constant_entry:").place(x=150, y=90)
    mult_constant_entry = Entry(frame3, textvariable=StringVar(value="1.0"))
    mult_constant_entry.place(x=270,y=90)

    ttk.Label(frame3, text="shift_constant_entry:").place(x=150, y=120)
    shift_constant_entry = Entry(frame3, textvariable=StringVar(value="0.0"))
    shift_constant_entry.place(x=270,y=120)

    ttk.Label(frame3, text="normalize_min_entry:").place(x=150, y=150)
    normalize_min_entry = Entry(frame3, textvariable=StringVar(value="-1.0"))
    normalize_min_entry.place(x=270,y=150)

    ttk.Label(frame3, text="normalize_max_entry:").place(x=150, y=180)
    normalize_max_entry = Entry(frame3, textvariable=StringVar(value="1.0"))
    normalize_max_entry.place(x=270,y=180)


    #Quantization 
   
    
    
    #handles selecting more than one file 
    def select_files():
        global selected_files
        file_paths = filedialog.askopenfilenames(filetypes=[("Text Files", "*.txt")])
        if file_paths:
            selected_files = file_paths
            print("selected files: ", select_files)
        else: 
            print("No Files Selected")
            
    

    result_label = Label(frame3, text="")
    result_label.pack()

    def execute_operation():
        try:
            selected_operation = operation_var.get()
            
            if not selected_files:
             result_label.config(text="No files selected.")

            if selected_operation in ["Multiplication", "Squaring", "Shifting", "Normalization", "Accumlation"]:
                if len(selected_files) != 1:
                    result_label.config(text="Select one file for multiplication/squaring/shifting/normalization/accumulation.")
            elif len(selected_files) != 2:
                result_label.config(text="Select two files for addition/subtraction.")

            if len(selected_files) > 0:
                x1, y1 = read_signal_file(selected_files[0])
            else:
                x1, y1 = None, None

            if len(selected_files) > 1:
                x2, y2 = read_signal_file(selected_files[1])
            else:
                x2, y2 = None, None
                

            print(selected_operation)
            print(selected_files)
           
            
            print("x1:", x1)
            print("y1:", y1)
            print("x2:", x2)
            print("y2:", y2)

            if selected_operation == "Addition":
                result_x, result_y = addition(x1, x2, y1, y2)
                plot_signal(x1, y1, "Signal 1")
                plot_signal(x2, y2, "Signal 2")
                plot_signal(result_x, result_y, "Result(Addition)")


            elif selected_operation == "Subtraction":
                result_x, result_y = subtraction(x1, x2, y1, y2)
                plot_signal(x1, y1, "Signal 1")
                plot_signal(x2, y2, "Signal 2")
                plot_signal(result_x, result_y, "Result (Subtraction)")


            elif selected_operation == "Multiplication":
                result_x, result_y = multiplication(x1, y1, float(mult_constant_entry.get()))
                plot_signal(x1, y1, "Signal 1")
                plot_signal(result_x, result_y, "Result (Multiplication)")


            elif selected_operation == "Squaring":
                if x1 is not None and y1 is not None:
                    result_x, result_y = squaring(x1, y1)
                    plot_signal(x1, y1, "Signal 1")
                    plot_signal(result_x, result_y, "Result (Squaring)")
                else:
                    result_label.config("bbbbaizzzz")


            elif selected_operation == "Shifting":
                shift_constant = float(shift_constant_entry.get())
                result_x, result_y = shift_signal(x1, y1, shift_constant)
                plot_signal(x1, y1, "Signal 1")
                plot_signal(result_x, result_y, "Result(Shifting)")


            elif selected_operation == "Normalization":
                result_y = normalize_signal(x1,y1, float(normalize_min_entry.get()), float(normalize_max_entry.get()))
                result_x=x1
                plot_signal(x1, y1, "Signal 1")
                plot_signal(x1, result_y, "Result (Normalization)")


            elif selected_operation == "Accumulation":
                result_x, result_y = accumlation(x1, y1)
                plot_signal(x1, y1, "Signal 1")
                plot_signal(result_x, result_y, "Result (Accumlation)")
            else:
                result_x, result_y = x1, y1

            # display_file_signal(result_x, result_y)
            result_label.config(text="Operation: " + selected_operation)
            
            SignalSamplesAreEqual('D:/DSP/Tasks/output signals/Signal1+signal2.txt',result_x,result_y)
            SignalSamplesAreEqual('D:/DSP/Tasks/output signals/signal1-signal2.txt',result_x,result_y)
            SignalSamplesAreEqual('D:/DSP/Tasks/output signals/MultiplySignalByConstant-Signal1 - by 5.txt',result_x,result_y)
            SignalSamplesAreEqual('D:/DSP/Tasks/output signals/Output squaring signal 1.txt',result_x,result_y)
            SignalSamplesAreEqual('D:/DSP/Tasks/output signals/output shifting by minus 500.txt',result_x,result_y)
            SignalSamplesAreEqual('D:/DSP/Tasks/output signals/output accumulation for signal1.txt',result_x,result_y)
            SignalSamplesAreEqual('D:/DSP/Tasks/output signals/normalize of signal 1 -- output.txt',x1,result_y)
            

        except Exception as e:
             print(f"ERROR:{str(e)}")
        
    ###Choosing file GUI    
    def choose_file():
        file_path = filedialog.askopenfilename(title="Choose a signal data file")
        if file_path:
            signal_x, signal_y = read_signal_file(file_path)
            return file_path, signal_x, signal_y
        else:
            return None, None, None
    
  
    choosefile=Button(frame3,text="Select file",command=lambda :select_files())
    execute_button = Button(frame3, text="Execute Operation", command=execute_operation)
    execute_button.place(x=300,y=300)
    choosefile.place(x=300,y=270)
    
    
    
    # Define global variables for signal data and DFT results
    signal_x = None
    signal_y = None
    frequencies = None  # Define frequencies as a global variable
    magnitude_spectrum = None
    phase_spectrum = None


    
    def apply_and_display_dft():
        global signal_x, signal_y, frequencies, magnitude_spectrum, phase_spectrum  # Declare frequencies as global

        try:
            filename=askopenfile()
            if filename is not None:
                print("File Selected: ",filename.name)
                x,y=read_signal_file(filename.name)
                sampling_frequency = float(sampling_frequency_entry.get())
                if x is not None and y is not None:
                    frequencies, magnitude_spectrum, phase_spectrum = apply_fourier_transform(sampling_frequency, x, y)
                    plot_signal_DFT(frequencies, magnitude_spectrum,"Amplitude spectrum")
                    plot_signal_DFT(frequencies, phase_spectrum,"Phase spectrum")
                    print("signal Data is loaded successfully in dft")
                else: 
                    print("Signal Data is NOT loaded in dft")
        except Exception as e:
            print(f"Error: {str(e)}")
           
           
    
        

    def apply_and_display_idft():
   
        try:
            _filename=askopenfile()
            if _filename is not None:
                print("File Selected: ",_filename.name)
                x,y=read_signal_file_IDFT(_filename.name)

                signal =IDFT(x,y)
                
                time=x 
                omega=ang_freq_gen(4,len(x))
                faze=y
                if x is not None and y is not None:
                    plot_signal_DFT(omega,time,"Time Domain")
                    print("signal Data is loaded successfully in idft----")
                    plot_signal_DFT(omega,faze,"m4 Time Domain")

                else: 
                    print("Signal Data is NOT loaded in idft")
        except Exception as e:
            print(f"Error: {str(e)}")
  
    
        
    def modify_and_display(new_freq,new_amp,new_phase):
        try:
                print("try")
                file_x,file_y=get_signals()
                new_amp = float(amplitude_entry.get())
                new_phase = float(phase_entry.get())
                file_x[int(new_freq)]=new_amp
                file_y[int(new_freq)]=new_phase
                print(IDFT(file_x,file_y))



        except Exception as e:
            print(f"Error: {str(e)}")

    
    def apply_shifting():
        x,y=get_signal_TimeDomain()
        plot_signal(x,y,"b4 shifting")
        #res,y=shift_signal(x,y,int(shift_const_entry.get()))  
        #res=shift_sig(x,int(shift_const_entry.get()))  
        shifted,y=shifting(x,y,int(shift_const_entry.get()))

        plot_signal(shifted,y,"shifted signal") 
        print("+500")
        ShiftSignalByConst(500,shifted,y)
        ShiftSignalByConst(-500,shifted,y)

    def apply_folding():
        indices,samples=get_signal_TimeDomain()
        
        plot_signal(indices,samples,"b4 folding")
        folded=fold_signal(samples)
        print(folded)
        plot_signal(indices,folded,"folded signal")
        SignalSamplesAreEqual("fold","TestCases_task6\Shifting_and_Folding\Output_fold.txt", indices, folded)

        
    def apply_folding_and_shifting():
        indices,samples=get_signal_TimeDomain()
        folded_signal=fold_signal(samples)
        shifted_signal,samples=shifting(indices,folded_signal,int(shift_const_entry.get()))
        plot_signal(indices,samples,"original")
        plot_signal(folded_signal,samples,"folded")
        plot_signal(shifted_signal,samples,"fold-shift")
        print(shifted_signal)
        # shift_Fold_Signal("D:\DSP\Tasks\TestCases_task6\Shifting_and_Folding\Output_ShifFoldedby500.txt",
        #                   shifted_signal,folded_signal)
        # shift_Fold_Signal("D:\DSP\Tasks\TestCases_task6\Shifting_and_Folding\Output_ShiftFoldedby-500.txt",
        #                   shifted_signal,folded_signal)

 
    def apply_convolution():
        x1, y1 = get_signal_TimeDomain()
        x2, y2 = get_signal_TimeDomain()
        conv,new_idx=convolve(x1,y1,x2,y2)
        print(conv)
        print(new_idx)
        plot_signal(x1,y1,"Signal 1")
        plot_signal(x2,y2,"Signal 2")
        plot_signal(new_idx,conv,"Convolved Signal")
        
        
    def apply_correlation():
        x1, y1 = get_signal_TimeDomain()
        x2, y2 = get_signal_TimeDomain()
        corr=normalized_cross_correlation(y1,y2)
        plot_signal(x1,y1,"Signal 1")
        plot_signal(x2,y2,"Signal 2")
        plot_signal(x1,corr,"Correlated Signal")
        Compare_Signals('Correlation\CorrOutput.txt', x1, corr)

            
    
    sampling_frequency_label = ttk.Label(frame5, text="Sampling Frequency (Hz)")
    sampling_frequency_label.pack(side="top", padx=10, pady=10)
    sampling_frequency_entry = ttk.Entry(frame5)
    sampling_frequency_entry.pack(side="top", padx=10, pady=10)

    apply_DFT_btn = ttk.Button(frame5, text="Apply DFT", command=apply_and_display_dft)
    apply_DFT_btn.pack(side="top", padx=10, pady=10)
    
    apply_IDFT_btn = ttk.Button(frame5, text="Apply IDFT", command=apply_and_display_idft)
    apply_IDFT_btn.pack(side="top", padx=10, pady=10)
    
  
    #modification input
    freq=IntVar()
    amp=IntVar()
    phase=IntVar()

    frequency_label = ttk.Label(frame5, text="frequency")
    frequency_label.pack(side="top", padx=10, pady=10)
    frequency_entry = tk.Entry(frame5,textvariable=freq)
    frequency_entry.pack(side="top", padx=10, pady=10)

    
    apmlitude_label = ttk.Label(frame5, text="Magnitude Spectrum")
    apmlitude_label.pack(side="top", padx=10, pady=10)
    amplitude_entry = tk.Entry(frame5,textvariable=amp)
    amplitude_entry.pack()

    phase_label = ttk.Label(frame5, text="Phase Spectrum")
    phase_label.pack(side="top", padx=10, pady=10)
    phase_entry = tk.Entry(frame5,textvariable=phase)
    phase_entry.pack(side="top", padx=10, pady=10)

    modify_button = ttk.Button(frame5, text="Modify and Update DFT", command=lambda:modify_and_display(frequency_entry.get(),amplitude_entry.get(),phase_entry.get()))
    modify_button.pack(side="top", padx=10, pady=10)
    
    apply_fur_idft = tk.Button(frame5, text="Compare",command=lambda: apply_comp())
    apply_fur_idft.pack(side="top",padx=10,pady=10)
    
    ############Task 5################################
    coeff_label=ttk.Label(frame5,text="enter coefficients")
    coeff_label.pack(side="top",padx=10,pady=10)
    coeff_entry=ttk.Entry(frame5)
    coeff_entry.pack(side="top",padx=10,pady=10)
    
    dct_btn=ttk.Button(frame5, text="Apply DCT", command=lambda:compute_dct(int(coeff_entry.get())))
    dct_btn.pack(side="top",padx=10,pady=10)
    
    remove_dc_btn=ttk.Button(frame5, text="remove dc", command=remove_dc_component)
    remove_dc_btn.pack(side="top",padx=10,pady=10)
    
   ###############Task 6###############################
   
    window_size=ttk.Label(frame6,text="Enter window size")
    window_size.pack(side="top",padx=10,pady=10)
    window_size_entry=ttk.Entry(frame6)
    window_size_entry.pack(side="top",padx=10,pady=10)
    
    smooth_btn=ttk.Button(frame6, text="Apply Smoothing", command=lambda:smoothing(int(window_size_entry.get())))
    smooth_btn.pack(side="top",padx=10,pady=10)

    shift_const=ttk.Label(frame6,text="enter shifting constant")
    shift_const.pack(side="top",padx=10,pady=10)
    shift_const_entry=ttk.Entry(frame6)
    shift_const_entry.pack(side="top",padx=10,pady=10)
    
    shift_btn=ttk.Button(frame6, text="Apply Shifting", command=apply_shifting)
    shift_btn.pack(side="top",padx=10,pady=10)
    
    fold_btn=ttk.Button(frame6, text="Apply Folding", command=apply_folding)
    fold_btn.pack(side="top",padx=10,pady=10)
    
    shift_fold_btn=ttk.Button(frame6, text="Apply Shifting on a Folded signal", command=apply_folding_and_shifting)
    shift_fold_btn.pack(side="top",padx=10,pady=10)

    remove_dc_btn=ttk.Button(frame6, text="Remove dc", command=remove_dc_time_domain)
    remove_dc_btn.pack(side="top",padx=10,pady=10)
    
    #####################TASK 7############################

    conv_btn=ttk.Button(frame6, text="Apply Convolution", command=apply_convolution)
    conv_btn.pack(side="top",padx=10,pady=10)
    
    #####################TASK 8############################
    corr_btn=ttk.Button(frame6, text="Apply Correlation", command=apply_correlation)
    corr_btn.pack(side="top",padx=10,pady=10)
    

    frame1.pack(fill=tk.BOTH, expand=True)
    frame2.pack(fill=tk.BOTH, expand=True)
    frame3.pack(fill=tk.BOTH, expand=True)
    frame4.pack(fill=tk.BOTH, expand=True)
    frame5.pack(fill=tk.BOTH, expand=True)
    frame6.pack(fill=tk.BOTH, expand=True)


    main_frame.add(frame1, text="file Input")
    main_frame.add(frame2, text="signal genration")
    main_frame.add(frame3, text="aritmatic opearations")
    main_frame.add(frame4, text="Siganl Quantization")
    main_frame.add(frame5, text="Frequency Domain")
    main_frame.add(frame6, text="Time Domain")
    


    main_frame.pack(expand=True, fill=tk.BOTH)

    def _exit():
        exit()

    menu = Menu(window)
    window.config(menu=menu)

    task1 = Menu(menu)
    menu.add_cascade(label="Menu", menu=task1)
    task1.add_command(label="exit", command=_exit)

    window.mainloop()

