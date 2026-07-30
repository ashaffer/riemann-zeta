import RHBridge.P2RoundedFlatFactorCheckpointData11

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel11FlatComponentChunk4 :
    P2RoundedFactorCheckpointData.panel11FlatEven4 =
      (P2RoundedFactorCheckpointData.panel11TruncatedEvenComponents).get ⟨4, by decide⟩ := by
  decide +kernel

theorem panel11FlatEven4_eq :
    P2RoundedFactorCheckpointData.panel11FlatEven4 =
      (P2RoundedFactorCheckpointData.panel11TruncatedEvenComponents).get ⟨4, by decide⟩ := by
  exact panel11FlatComponentChunk4

end RHP2Bridge
