import RHBridge.P2RoundedFactorCheckpointData31

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel31FactorChunk10 :
    P2RoundedFactorCheckpointData.panel31Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨31, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel31Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨31, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel31Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨31, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel31Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨31, by decide⟩ := by
  decide +kernel

theorem panel31Prefix40_eq :
    P2RoundedFactorCheckpointData.panel31Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk10.1

theorem panel31Prefix41_eq :
    P2RoundedFactorCheckpointData.panel31Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk10.2.1

theorem panel31Prefix42_eq :
    P2RoundedFactorCheckpointData.panel31Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk10.2.2.1

theorem panel31Prefix43_eq :
    P2RoundedFactorCheckpointData.panel31Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk10.2.2.2

end RHP2Bridge
