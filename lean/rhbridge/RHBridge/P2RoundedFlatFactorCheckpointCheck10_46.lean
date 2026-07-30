import RHBridge.P2RoundedFlatFactorCheckpointData10

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel10FlatComponentChunk46 :
    P2RoundedFactorCheckpointData.panel10FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel10TruncatedOddComponents).get ⟨22, by decide⟩ := by
  decide +kernel

theorem panel10FlatOdd22_eq :
    P2RoundedFactorCheckpointData.panel10FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel10TruncatedOddComponents).get ⟨22, by decide⟩ := by
  exact panel10FlatComponentChunk46

end RHP2Bridge
