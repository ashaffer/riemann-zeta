import RHBridge.P2RoundedFlatFactorCheckpointData10

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel10FlatComponentChunk36 :
    P2RoundedFactorCheckpointData.panel10FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel10TruncatedOddComponents).get ⟨12, by decide⟩ := by
  decide +kernel

theorem panel10FlatOdd12_eq :
    P2RoundedFactorCheckpointData.panel10FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel10TruncatedOddComponents).get ⟨12, by decide⟩ := by
  exact panel10FlatComponentChunk36

end RHP2Bridge
