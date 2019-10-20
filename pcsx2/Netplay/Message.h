#pragma once
#include "EmulatorState.h"
#include "shoryu/archive.h"

struct Message
{
	Message();
	char input[6];
	void serialize(shoryu::oarchive& a) const;
	void deserialize(shoryu::iarchive& a);
};
