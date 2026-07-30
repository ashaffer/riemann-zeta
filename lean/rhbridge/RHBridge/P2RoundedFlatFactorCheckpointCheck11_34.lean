import RHBridge.P2RoundedFlatFactorCheckpointData11

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel11FlatComponentChunk34 :
    P2RoundedFactorCheckpointData.panel11FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel11TruncatedOddComponents).get ⟨10, by decide⟩ := by
  decide +kernel

theorem panel11FlatOdd10_eq :
    P2RoundedFactorCheckpointData.panel11FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel11TruncatedOddComponents).get ⟨10, by decide⟩ := by
  exact panel11FlatComponentChunk34

end RHP2Bridge
