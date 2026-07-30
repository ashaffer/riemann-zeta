import RHBridge.P2RoundedFlatFactorCheckpointData11

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel11FlatComponentChunk31 :
    P2RoundedFactorCheckpointData.panel11FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel11TruncatedOddComponents).get ⟨7, by decide⟩ := by
  decide +kernel

theorem panel11FlatOdd7_eq :
    P2RoundedFactorCheckpointData.panel11FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel11TruncatedOddComponents).get ⟨7, by decide⟩ := by
  exact panel11FlatComponentChunk31

end RHP2Bridge
