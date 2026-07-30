import RHBridge.P2RoundedFlatFactorCheckpointData10

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel10FlatComponentChunk21 :
    P2RoundedFactorCheckpointData.panel10FlatEven21 =
      (P2RoundedFactorCheckpointData.panel10TruncatedEvenComponents).get ⟨21, by decide⟩ := by
  decide +kernel

theorem panel10FlatEven21_eq :
    P2RoundedFactorCheckpointData.panel10FlatEven21 =
      (P2RoundedFactorCheckpointData.panel10TruncatedEvenComponents).get ⟨21, by decide⟩ := by
  exact panel10FlatComponentChunk21

end RHP2Bridge
