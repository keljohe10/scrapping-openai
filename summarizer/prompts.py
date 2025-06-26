def system_prompt():
    return (
        "You are an assistant that analyzes the contents of a website "
        "and provides a short summary, ignoring text that might be navigation related. "
        "Respond in plain text."
    )

def user_prompt_for(website):
    return (
        f"You are looking at a website titled {website.title}\n"
        "The contents of this website is as follows; "
        "please provide a short summary of this website. "
        "If it includes news or announcements, then summarize these too.\n\n"
        + website.text
    )

def messages_for(website):
    return [
        {"role": "system", "content": system_prompt()},
        {"role": "user", "content": user_prompt_for(website)}
    ]
