import RHBridge.P2RoundedFactorCheckpointData1

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel1FactorChunk10 :
    P2RoundedFactorCheckpointData.panel1Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨1, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel1Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨1, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel1Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨1, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel1Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨1, by decide⟩ := by
  decide +kernel

theorem panel1Prefix40_eq :
    P2RoundedFactorCheckpointData.panel1Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk10.1

theorem panel1Prefix41_eq :
    P2RoundedFactorCheckpointData.panel1Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk10.2.1

theorem panel1Prefix42_eq :
    P2RoundedFactorCheckpointData.panel1Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk10.2.2.1

theorem panel1Prefix43_eq :
    P2RoundedFactorCheckpointData.panel1Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk10.2.2.2

end RHP2Bridge
