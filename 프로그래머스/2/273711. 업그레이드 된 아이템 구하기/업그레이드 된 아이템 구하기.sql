select I.ITEM_ID,	I.ITEM_NAME,	I.RARITY 
from ITEM_TREE T 
join ITEM_INFO I on I.ITEM_ID =T.ITEM_ID
join ITEM_INFO C on C.ITEM_ID=T.PARENT_ITEM_ID
where C.RARITY='RARE'
order by I.ITEM_ID desc;

