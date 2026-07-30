import RHBridge.P2RoundedFlatFactorCheckpointData10

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel10FlatComponentChunk38 :
    P2RoundedFactorCheckpointData.panel10FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel10TruncatedOddComponents).get ⟨14, by decide⟩ := by
  decide +kernel

theorem panel10FlatOdd14_eq :
    P2RoundedFactorCheckpointData.panel10FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel10TruncatedOddComponents).get ⟨14, by decide⟩ := by
  exact panel10FlatComponentChunk38

end RHP2Bridge
