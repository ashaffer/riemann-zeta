import RHBridge.P2RoundedFlatFactorCheckpointData10

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel10FlatComponentChunk17 :
    P2RoundedFactorCheckpointData.panel10FlatEven17 =
      (P2RoundedFactorCheckpointData.panel10TruncatedEvenComponents).get ⟨17, by decide⟩ := by
  decide +kernel

theorem panel10FlatEven17_eq :
    P2RoundedFactorCheckpointData.panel10FlatEven17 =
      (P2RoundedFactorCheckpointData.panel10TruncatedEvenComponents).get ⟨17, by decide⟩ := by
  exact panel10FlatComponentChunk17

end RHP2Bridge
