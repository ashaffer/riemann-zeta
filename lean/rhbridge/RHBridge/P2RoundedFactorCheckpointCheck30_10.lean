import RHBridge.P2RoundedFactorCheckpointData30

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel30FactorChunk10 :
    P2RoundedFactorCheckpointData.panel30Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨30, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel30Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨30, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel30Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨30, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel30Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨30, by decide⟩ := by
  decide +kernel

theorem panel30Prefix40_eq :
    P2RoundedFactorCheckpointData.panel30Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk10.1

theorem panel30Prefix41_eq :
    P2RoundedFactorCheckpointData.panel30Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk10.2.1

theorem panel30Prefix42_eq :
    P2RoundedFactorCheckpointData.panel30Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk10.2.2.1

theorem panel30Prefix43_eq :
    P2RoundedFactorCheckpointData.panel30Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk10.2.2.2

end RHP2Bridge
