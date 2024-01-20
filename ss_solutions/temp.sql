select
    COUNT(request_id)
from
    (
        select
            request_id,
            count(created_on)
        from
            redfin_call_tracking
        where
            HOUR(created_on) between 15 and 18
        group by
            request_id
        having
            count(created_on) >= 3
    ) as temp_Q


    