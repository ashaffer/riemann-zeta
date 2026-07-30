import RHBridge.P2RoundedFlatFactorCheckpointData10

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel10FlatComponentChunk27 :
    P2RoundedFactorCheckpointData.panel10FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel10TruncatedOddComponents).get ⟨3, by decide⟩ := by
  decide +kernel

theorem panel10FlatOdd3_eq :
    P2RoundedFactorCheckpointData.panel10FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel10TruncatedOddComponents).get ⟨3, by decide⟩ := by
  exact panel10FlatComponentChunk27

end RHP2Bridge
