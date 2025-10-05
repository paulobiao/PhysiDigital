
def score_event(e):
    score = 0; reasons=[]; flags={}
    v = e.get('value', 0.0)
    metric = e.get('metric','')
    if metric=='temperature' and (v<0 or v>60):
        score+=30; reasons.append('TEMP_OUT_OF_RANGE'); flags['temp_oob']=True
    if metric=='power' and v>10000:
        score+=25; reasons.append('POWER_SPIKE'); flags['power_spike']=True
    if metric=='flow' and v==0:
        score+=10; reasons.append('FLOW_ZERO'); flags['flow_zero']=True
    if e.get('token') != 'agent-demo-token':
        score+=20; reasons.append('BAD_TOKEN'); flags['bad_token']=True
    if score==0: reasons.append('LOW_RISK_BASELINE')
    return min(score,100), reasons, flags
