import RHBridge.P2RoundedFlatFactorCheckpointData11

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel11FlatComponentChunk24 :
    P2RoundedFactorCheckpointData.panel11FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel11TruncatedOddComponents).get ⟨0, by decide⟩ := by
  decide +kernel

theorem panel11FlatOdd0_eq :
    P2RoundedFactorCheckpointData.panel11FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel11TruncatedOddComponents).get ⟨0, by decide⟩ := by
  exact panel11FlatComponentChunk24

end RHP2Bridge
