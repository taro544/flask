import datetime
import time

# Specify target date and time
target_date = datetime.datetime(2023, 5, 14, 8, 00, 00)


# Calculate remaining time
current_time = datetime.datetime.now()
time_diff = target_date - current_time
days = time_diff.days
hours, remainder = divmod(time_diff.seconds, 3600)
minutes, seconds = divmod(remainder, 60)
    
# Display remaining time
output_str = estimated_time = f"Secime son {time_diff.days} gun, {hours} saat, {minutes} dakika, {seconds} saniye" 
print(output_str)
