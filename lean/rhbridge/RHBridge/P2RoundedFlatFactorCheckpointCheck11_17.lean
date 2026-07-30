import RHBridge.P2RoundedFlatFactorCheckpointData11

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel11FlatComponentChunk17 :
    P2RoundedFactorCheckpointData.panel11FlatEven17 =
      (P2RoundedFactorCheckpointData.panel11TruncatedEvenComponents).get ⟨17, by decide⟩ := by
  decide +kernel

theorem panel11FlatEven17_eq :
    P2RoundedFactorCheckpointData.panel11FlatEven17 =
      (P2RoundedFactorCheckpointData.panel11TruncatedEvenComponents).get ⟨17, by decide⟩ := by
  exact panel11FlatComponentChunk17

end RHP2Bridge
