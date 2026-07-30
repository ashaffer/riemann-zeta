import RHBridge.P2RoundedFlatFactorCheckpointData10

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel10FlatComponentChunk23 :
    P2RoundedFactorCheckpointData.panel10FlatEven23 =
      (P2RoundedFactorCheckpointData.panel10TruncatedEvenComponents).get ⟨23, by decide⟩ := by
  decide +kernel

theorem panel10FlatEven23_eq :
    P2RoundedFactorCheckpointData.panel10FlatEven23 =
      (P2RoundedFactorCheckpointData.panel10TruncatedEvenComponents).get ⟨23, by decide⟩ := by
  exact panel10FlatComponentChunk23

end RHP2Bridge
