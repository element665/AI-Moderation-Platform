def process_comment(comment):
    result = classify(comment["text"])
    action = apply_rules(result)
    execute_action(action, comment)
    save_to_db(comment, result)