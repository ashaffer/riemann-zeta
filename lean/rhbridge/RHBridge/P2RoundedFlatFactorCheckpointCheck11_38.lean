import RHBridge.P2RoundedFlatFactorCheckpointData11

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel11FlatComponentChunk38 :
    P2RoundedFactorCheckpointData.panel11FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel11TruncatedOddComponents).get ⟨14, by decide⟩ := by
  decide +kernel

theorem panel11FlatOdd14_eq :
    P2RoundedFactorCheckpointData.panel11FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel11TruncatedOddComponents).get ⟨14, by decide⟩ := by
  exact panel11FlatComponentChunk38

end RHP2Bridge
