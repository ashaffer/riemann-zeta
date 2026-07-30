import RHBridge.P2RoundedFlatFactorCheckpointData1

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel1FlatComponentChunk28 :
    P2RoundedFactorCheckpointData.panel1FlatOdd4 =
      (P2RoundedFactorCheckpointData.panel1TruncatedOddComponents).get ⟨4, by decide⟩ := by
  decide +kernel

theorem panel1FlatOdd4_eq :
    P2RoundedFactorCheckpointData.panel1FlatOdd4 =
      (P2RoundedFactorCheckpointData.panel1TruncatedOddComponents).get ⟨4, by decide⟩ := by
  exact panel1FlatComponentChunk28

end RHP2Bridge
