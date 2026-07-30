import RHBridge.P2RoundedFlatFactorCheckpointData11

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel11FlatComponentChunk0 :
    P2RoundedFactorCheckpointData.panel11FlatEven0 =
      (P2RoundedFactorCheckpointData.panel11TruncatedEvenComponents).get ⟨0, by decide⟩ := by
  decide +kernel

theorem panel11FlatEven0_eq :
    P2RoundedFactorCheckpointData.panel11FlatEven0 =
      (P2RoundedFactorCheckpointData.panel11TruncatedEvenComponents).get ⟨0, by decide⟩ := by
  exact panel11FlatComponentChunk0

end RHP2Bridge
