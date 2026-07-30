import RHBridge.P2RoundedFactorCheckpointData14

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel14FactorChunk10 :
    P2RoundedFactorCheckpointData.panel14Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨14, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel14Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨14, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel14Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨14, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel14Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨14, by decide⟩ := by
  decide +kernel

theorem panel14Prefix40_eq :
    P2RoundedFactorCheckpointData.panel14Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk10.1

theorem panel14Prefix41_eq :
    P2RoundedFactorCheckpointData.panel14Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk10.2.1

theorem panel14Prefix42_eq :
    P2RoundedFactorCheckpointData.panel14Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk10.2.2.1

theorem panel14Prefix43_eq :
    P2RoundedFactorCheckpointData.panel14Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk10.2.2.2

end RHP2Bridge
