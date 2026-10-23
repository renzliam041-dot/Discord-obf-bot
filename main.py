-- No longer use ASCII encoding; instead use bytecode
local func = loadstring(raw_code)  -- First load the source code
local bytecode = string.dump(func) -- Convert to bytecode binary
-- Then encode the bytecode as an escaped string
local escaped = bytecode:gsub(".", function(c)
    return string.format("\\%d", string.byte(c))
end)
result_code = 'loadstring("' .. escaped .. '")()'
