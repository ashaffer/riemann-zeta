import RHBridge.P2RoundedFlatFactorCheckpointData11

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel11FlatComponentChunk27 :
    P2RoundedFactorCheckpointData.panel11FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel11TruncatedOddComponents).get ⟨3, by decide⟩ := by
  decide +kernel

theorem panel11FlatOdd3_eq :
    P2RoundedFactorCheckpointData.panel11FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel11TruncatedOddComponents).get ⟨3, by decide⟩ := by
  exact panel11FlatComponentChunk27

end RHP2Bridge
