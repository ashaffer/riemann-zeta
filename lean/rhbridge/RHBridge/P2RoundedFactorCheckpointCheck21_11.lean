import RHBridge.P2RoundedFactorCheckpointData21

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel21FactorChunk11 :
    P2RoundedFactorCheckpointData.panel21Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨21, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel21Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨21, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel21Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨21, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel21Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨21, by decide⟩ := by
  decide +kernel

theorem panel21Prefix44_eq :
    P2RoundedFactorCheckpointData.panel21Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk11.1

theorem panel21Prefix45_eq :
    P2RoundedFactorCheckpointData.panel21Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk11.2.1

theorem panel21Prefix46_eq :
    P2RoundedFactorCheckpointData.panel21Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk11.2.2.1

theorem panel21Prefix47_eq :
    P2RoundedFactorCheckpointData.panel21Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk11.2.2.2

end RHP2Bridge
