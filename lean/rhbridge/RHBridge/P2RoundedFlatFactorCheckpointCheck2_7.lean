import RHBridge.P2RoundedFlatFactorCheckpointData2

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel2FlatComponentChunk7 :
    P2RoundedFactorCheckpointData.panel2FlatEven7 =
      (P2RoundedFactorCheckpointData.panel2TruncatedEvenComponents).get ⟨7, by decide⟩ := by
  decide +kernel

theorem panel2FlatEven7_eq :
    P2RoundedFactorCheckpointData.panel2FlatEven7 =
      (P2RoundedFactorCheckpointData.panel2TruncatedEvenComponents).get ⟨7, by decide⟩ := by
  exact panel2FlatComponentChunk7

end RHP2Bridge
