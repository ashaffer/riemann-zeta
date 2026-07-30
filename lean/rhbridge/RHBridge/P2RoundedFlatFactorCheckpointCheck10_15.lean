import RHBridge.P2RoundedFlatFactorCheckpointData10

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel10FlatComponentChunk15 :
    P2RoundedFactorCheckpointData.panel10FlatEven15 =
      (P2RoundedFactorCheckpointData.panel10TruncatedEvenComponents).get ⟨15, by decide⟩ := by
  decide +kernel

theorem panel10FlatEven15_eq :
    P2RoundedFactorCheckpointData.panel10FlatEven15 =
      (P2RoundedFactorCheckpointData.panel10TruncatedEvenComponents).get ⟨15, by decide⟩ := by
  exact panel10FlatComponentChunk15

end RHP2Bridge
