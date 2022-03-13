
min = 00
sec = 00
hrs = 00

while true do
    puts "Time Elapsed: #{hrs}:#{min}:#{sec}"
    sec +=1
    sleep(1)
    if sec == 60
        sec = 0
        min += 1
    end

    if min == 60
        min =0
        hrs +=1

    end

    if hrs == 12
        hrs = 0

    end

end


