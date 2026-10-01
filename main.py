import clr
import psutil

clr.AddReference(r".\LibreHardwareMonitor\LibreHardwareMonitorLib")

from LibreHardwareMonitor.Hardware import Computer

computer = Computer()
computer.IsGpuEnabled = True
computer.IsCpuEnabled = True

computer.Open()
while True:
     cpu_usage = psutil.cpu_percent(interval=1)
     ram_usage = psutil.virtual_memory()
     Cpu_Temperature = None
     gpu_temperature = {}
     gpu_usage = {}

     for hardware in computer.Hardware:
         hardware.Update()
         for sensor in hardware.Sensors:
        
             if(
                 str(hardware.HardwareType).startswith("Gpu")
                 and str(sensor.SensorType) == "Temperature"
                 and sensor.Name == "GPU Core"
               ):
                 gpu_temperature[hardware.Name] = sensor.Value


             if(
                 str(hardware.HardwareType).startswith("Gpu")
                 and str(sensor.SensorType) == "Load"
                 and sensor.Name == "GPU Core"
               ):
                 gpu_usage[hardware.Name] = sensor.Value


             if (
                 str(hardware.HardwareType) == "Cpu"
                 and str(sensor.SensorType) == "Temperature" 
                 and sensor.Name == "CPU Package"
                ):
                 Cpu_Temperature = sensor.Value


     print(f"Cpu Usage = {cpu_usage}%")
     print(f"Ram Usage = {ram_usage.percent}%")
     print(f"Cpu Temperature = {Cpu_Temperature}°C")

     for gpu_name in gpu_usage:
         print(f"{gpu_name} usage = {gpu_usage.get(gpu_name)}%")
         print(f"{gpu_name} Temperature = {gpu_temperature.get(gpu_name)}°C")
        

         
