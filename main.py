local lastTouched = 0

script.Parent.Touched:Connect(function(HumPart)
	local currentTime = tick() -- Get the current time
	
	if not HumPart.Parent:FindFirstChildOfClass("Humanoid") then
		return
	end
	if currentTime - lastTouched < 1 then
		return
	end

	lastTouched = currentTime

	for _, item in ipairs(script.Parent.Parent:GetChildren()) do
		if item:IsA("Accessory") and not HumPart.Parent:FindFirstChild(item.Name) then
			local cloned = item:Clone()
			cloned.Parent = HumPart.Parent
		end
	end
end)
