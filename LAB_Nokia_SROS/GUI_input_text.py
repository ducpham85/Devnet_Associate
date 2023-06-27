import tkinter as tk
import paramiko

def send_command():
    command = command_entry.get()
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, f"Command: {command}\n\n")

    # try:
    #     ssh_client = paramiko.SSHClient()
    #     ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     ssh_client.connect(hostname="your_router_ip", username="your_username", password="your_password")
    #     stdin, stdout, stderr = ssh_client.exec_command(command)
    #     output = stdout.read().decode()
    #     output_text.insert(tk.END, output)
    #     ssh_client.close()
    # except paramiko.AuthenticationException:
    #     output_text.insert(tk.END, "Authentication failed.")
    # except paramiko.SSHException as ssh_exc:
    #     output_text.insert(tk.END, f"SSH error occurred: {ssh_exc}")
    # except paramiko.Exception as exc:
    #     output_text.insert(tk.END, f"An error occurred: {exc}")

    output_text.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Router Command Sender")

# Command entry field
command_entry = tk.Entry(root, width=40)
command_entry.pack()

# Send button
send_button = tk.Button(root, text="Send", command=send_command)
send_button.pack()

# Output text widget
output_text = tk.Text(root, height=10, width=40)
output_text.config(state=tk.DISABLED)
output_text.pack()

root.mainloop()
