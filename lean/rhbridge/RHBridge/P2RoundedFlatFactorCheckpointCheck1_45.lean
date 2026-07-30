import RHBridge.P2RoundedFlatFactorCheckpointData1

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel1FlatComponentChunk45 :
    P2RoundedFactorCheckpointData.panel1FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel1TruncatedOddComponents).get ⟨21, by decide⟩ := by
  decide +kernel

theorem panel1FlatOdd21_eq :
    P2RoundedFactorCheckpointData.panel1FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel1TruncatedOddComponents).get ⟨21, by decide⟩ := by
  exact panel1FlatComponentChunk45

end RHP2Bridge
